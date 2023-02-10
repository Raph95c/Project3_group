#--------------#
# Dependencies #
#--------------#

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, join
from datetime import date
from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

#----------------#
# Database Setup #
#----------------#
engine = create_engine("sqlite:///Resources/earthquakes.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# View all of the classes that automap found
Base.classes.keys()

# Save reference to eq_data table
eq_data = Base.classes.eq_data

#-------------#
# Flask setup #
#-------------#
app = Flask(__name__)

#--------------#
# Flask Routes #
#--------------#

@app.route("/")
def home():
    return (
        f"Welcome to the Earthquate app!<br/>"
        f"Available endpoints:<br/>"
        f"/api/v1.0/allearthquakes<br/>"
        f"/api/v1.0/mag3to4earthquakes<br/>"
        f"/api/v1.0/mag41to5earthquakes<br/>"
        f"/api/v1.0/mag51to6earthquakes<br/>"
        f"/api/v1.0/mag61to7earthquakes<br/>"
        f"/api/v1.0/mag71andgreaterearthquakes<br/>"
    )

#------------------------------#
# All Earthquakes              #
#------------------------------#

@app.route("/api/v1.0/allearthquakes")
def allearthquakes():
    # Create a session
    session = Session(engine)

    # Query the database for earthquake data with magnitude between 3.0 and 4.0
    all_results = session.query(
                            eq_data.place,
                            eq_data.mag
                            ).filter(eq_data.mag >= 3.0,
                            eq_data.mag <= 4.0).all()

    # Close the session
    session.close()

    all_earthquakes = []
    for place, mag in all_results:
        all_earthquakes_dict = {}
        all_earthquakes_dict["Magnitude"] = mag
        all_earthquakes_dict["Place"] = place
        all_earthquakes.append(all_earthquakes_dict)

    # Return the results as a JSON object
    return jsonify(all_earthquakes)


#------------------------------#
# Magnitude 3.0-4.0 Route      #
#------------------------------#

@app.route("/api/v1.0/mag3to4earthquakes")
def mag3to4():
    # Create a session
    session = Session(engine)

    # Query the database for earthquake data with magnitude between 3.0 and 4.0
    all_results = session.query(
                            eq_data.place,
                            eq_data.mag
                            ).filter(eq_data.mag >= 3.0,
                            eq_data.mag <= 4.0).all()

    # Close the session
    session.close()

    mag3_4_earthquakes = []
    for place, mag in all_results:
        mag3_4_earthquakes_dict = {}
        mag3_4_earthquakes_dict["Magnitude"] = mag
        mag3_4_earthquakes_dict["Place"] = place
        mag3_4_earthquakes.append(mag3_4_earthquakes_dict)

    # Return the results as a JSON object
    return jsonify(mag3_4_earthquakes)

#------------------------------#
# Magnitude 4.1-5.0 Route      #
#------------------------------#

@app.route("/api/v1.0/mag41to5earthquakes")
def mag4to5():
    # Create a session
    session = Session(engine)

    # Query the database for earthquake data with magnitude between 4.1 and 5.0
    all_results = session.query(
                            eq_data.mag,
                            eq_data.place,
                            eq_data.depth
                            ).filter(eq_data.mag >= 4.1,
                            eq_data.mag <= 5.0).all()

    # Close the session
    session.close()

    mag4_5_earthquakes = []
    for place, depth,mag in all_results:
        mag4_5_earthquakes_dict = {}
        mag4_5_earthquakes_dict["Magnitude"] = mag
        mag4_5_earthquakes_dict["Place"] = place
        mag4_5_earthquakes_dict["Depth"] = depth
        mag4_5_earthquakes.append(mag4_5_earthquakes_dict)

    # Return the results as a JSON object
    return jsonify(mag4_5_earthquakes)

#---------------#
# Main behavior #
#---------------#
if __name__ == "__main__":
    app.run(debug=True)