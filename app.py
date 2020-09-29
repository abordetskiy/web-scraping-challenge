# Import Dependencies
from flask import Flask, render_template
import pandas as pd
import pymongo
# Import scrapeData() function from mission_to_mars.ipynb
# May need to pip install ipynb
from ipynb.fs.defs.Mission_to_Mars import scrapeData

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
########################### mongo_Variable = PyMongo(app, uri="mongodb://localhost:27017/DATABASE_NAME")


# Route to render index.html template
@app.route("/")
def index():
    links = client.mars_db.web_links.find()
    print("Homepage Accessed")
    # Return template and data
    return render_template("index.html", links=links)

@app.route("/scrape")
def scrape():
    # Run Data Scraper function from mission_to_mars.ipynb
    scrapeData()
    # 
    links = client.mars_db.web_links.find()
    # Return template and data
    return render_template("index.html", links=links)

if __name__ == "__main__":
    app.run(debug=False)