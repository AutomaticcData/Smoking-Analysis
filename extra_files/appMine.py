import os

import pymongo
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = "mongodb://localhost:27017"

client = pymongo.MongoClient(conn)
db = client.smoking

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/collections/avgpricepack")
def avgpricepack_json():
    print(db)
    avgpricepack = list(db.avgpricepack.find({}, {'_id': False}))
    print(avgpricepack)
    return jsonify(avgpricepack)

if __name__ == "__main__":
    app.run()