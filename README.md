## Project 3: California Earthquakes – Is the next big one coming?

# Group 1 Team Members: Robert Hascall, Quoc Tran, Alexis Valdez, Kelly Stave, Raymundo Zapien
Overview:

# The title of our project is: California Earthquakes - Is the next big one coming?

The aim of our project is to determine if there has been a change in the frequency and severity of earthquakes in California over the last 20 years. We will examine the following questions:

1. Has there been an increase in the number of earthquakes in the last 20 years?
2. Have earthquakes intensified in the last 20 years?
3. Is there a correlation between magnitude and depth of an earthquake?

The dataset used included earthquakes with a magnitude of 3.0 or greater.  The reason for this is that earthquakes can be felt by us humans beginning at magnitude 3.0.

Reference data source:
USGS.gov

GeoJSON url: 
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2000-01-01&endtime=2023-01-01&minmagnitude=3&eventtype=earthquake&minlatitude=32.5&minlongitude=-124&maxlatitude=42.0&maxlongitude=-114.5

Parameters:
* Start Date: 2000-01-01
* End Date: 2023-01-01
* Format: geoJSON
* Min Magnitude: 3
* Event Type: earthquake
* Min Latitude: 32.5
* Min Longitude -12.4
* Max Latitude: 42.0
* Max Longitude: -114.5

# Methods:
* Sqlite was used to house the data after it had been downloaded in csv format which was then loaded into a list of tuples.   Sqlite3 was loaded as a dependency to then create a table in the earthquakes database which was also created.  The data from the aforementioned list of tuples was then INSERTed into the table.  All charts and plots were created from this database.

* HTML pages and css, along with javascript were used to access the USGS data via a geoJSON call.  For mapping, map layers were retrieved from openstreetmap.org and opentopomap.org to display earthquake coordinates with latitude and longitude data by selecting either a streetmap or topographical map.

* Flask was used to serve the HTML pages, css and javascript. 

# Analysis:
The overall analysis was that "The big one" is not imminent based on the data. While two years showed an increase in earthquake activity (in 3.0 magnitudes or greater), these could be outliers since the dataset included twenty-three years in which there was a much lower ebb-and-flow of earthquake activity.  This information can be seen in the chart Earthquake Count by Year > 3.0.

Further, the average magnitude by year remained steady, over the time range of between 3.3 and 3.5.  Additionally, the vast majority, 91.1% of earthquakes are within the range 3.0 to 4.0 and magnitudes 4.0 to 5.0 account for 8.3% of all quakes over that period.  While it only takes one "big one", the data would appear to show that there is no imminent danger of the "big one" occurring in the near term.

Finally, analysis of magnitude vs. depth did not appear to show any correlation between magnitude and depth.

