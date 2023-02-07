#--------------#
# Dependencies #
#--------------#

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, join
from datetime import date
from flask import Flask, jsonify

#----------------#
# Database Setup #
#----------------#
engine = create_engine("sqlite:///Resources/earthquakes.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
print(Base.classes.keys())

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
        f"/api/v1.0/mag3to4earthquakes<br/>"
        f"/api/v1.0/mag41to5earthquakes<br/>"
        f"/api/v1.0/mag51to6earthquakes<br/>"
        f"/api/v1.0/mag61to7earthquakes<br/>"
        f"/api/v1.0/mag71andgreaterearthquakes<br/>"
    )

#------------------------------#
# Magnitude 3.0-4.0 Route      #
#------------------------------#

@app.route("/api/v1.0/mag3to4earthquakes")
def mag3to4():
    # Create a session
    session = Session(engine)

    # Query the database for earthquake data with magnitude between 3.0 and 4.0
    results = session.query(eq_data).filter(eq_data.mag >= 3.0, eq_data.mag < 4.0).all()

    # Close the session
    session.close()

    # Convert the results to a list of dictionaries
    earthquake_list = [result.__dict__ for result in results]

    # Return the results as a JSON object
    return jsonify(earthquake_list)

#---------------#
# Main behavior #
#---------------#
if __name__ == "__main__":
    app.run(debug=True)