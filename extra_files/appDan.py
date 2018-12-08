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
  avgpricepack = list(db.avgpricepack.find({}, {'_id': False}))
  return jsonify(avgpricepack)

@app.route("/collections/comparemenwomensmoking")
def comparemenwomensmoking_json():
  comparemenwomensmoking = list(db.comparemenwomensmoking.find({}, {'_id': False}))
  return jsonify(comparemenwomensmoking)

@app.route("/collections/consumepersmokerperday")
def consumepersmokerperday_json():
  consumepersmokerperday = list(db.consumepersmokerperday.find({}, {'_id': False}))
  return jsonify(consumepersmokerperday)

@app.route("/collections/consumepersmokerperdaybounds")
def consumepersmokerperdaybounds_json():
  consumepersmokerperdaybounds = list(db.consumepersmokerperdaybounds.find({}, {'_id': False}))
  return jsonify(consumepersmokerperdaybounds)

@app.route("/collections/dailysmokingprevbounds")
def dailysmokingprevbounds_json():
  dailysmokingprevbounds = list(db.dailysmokingprevbounds.find({}, {'_id': False}))
  return jsonify(dailysmokingprevbounds)

@app.route("/collections/enforcebanstobacad")
def enforcebanstobacad_json():
  enforcebanstobacad = list(db.enforcebanstobacad.find({}, {'_id': False}))
  return jsonify(enforcebanstobacad)

@app.route("/collections/healthyagingdata")
def healthyagingdata_json():
  healthyagingdata = list(db.healthyagingdata.find({}, {'_id': False}))
  return jsonify(healthyagingdata)

@app.route("/collections/numdeathssecondhand")
def numdeathssecondhand_json():
  numdeathssecondhand = list(db.numdeathssecondhand.find({}, {'_id': False}))
  return jsonify(numdeathssecondhand)

@app.route("/collections/numdeathstobaccosmoking")
def numdeathstobaccosmoking_json():
  numdeathstobaccosmoking = list(db.numdeathstobaccosmoking.find({}, {'_id': False}))
  return jsonify(numdeathstobaccosmoking)

@app.route("/collections/numtotaldailysmokers")
def numtotaldailysmokers_json():
  numtotaldailysmokers = list(db.numtotaldailysmokers.find({}, {'_id': False}))
  return jsonify(numtotaldailysmokers)

@app.route("/collections/salesofcigsperadultperday")
def salesofcigsperadultperday():
  salesofcigsperadultperday = list(db.salesofcigsperadultperday.find({}, {'_id': False}))
  return jsonify(salesofcigsperadultperday)

@app.route("/collections/secondhandsmokedeathsbyage")
def secondhandsmokedeathsbyage():
  secondhandsmokedeathsbyage = list(db.secondhandsmokedeathsbyage.find({}, {'_id': False}))
  return jsonify(secondhandsmokedeathsbyage)

@app.route("/collections/sharecancerdeathsfromtobacco")
def sharecancerdeathsfromtobacco():
  sharecancerdeathsfromtobacco = list(db.sharecancerdeathsfromtobacco.find({}, {'_id': False}))
  return jsonify(sharecancerdeathsfromtobacco)

@app.route("/collections/sharemensmoking")
def sharemensmoking():
  sharemensmoking = list(db.sharemensmoking.find({}, {'_id': False}))
  return jsonify(sharemensmoking)

@app.route("/collections/sharemensmokinglevelprosperity")
def sharemensmokinglevelprosperity():
  sharemensmokinglevelprosperity = list(db.sharemensmokinglevelprosperity.find({}, {'_id': False}))
  return jsonify(sharemensmokinglevelprosperity)

@app.route("/collections/sharetobaccoretailpricetax")
def sharetobaccoretailpricetax():
  sharetobaccoretailpricetax = list(db.sharetobaccoretailpricetax.find({}, {'_id': False}))
  return jsonify(sharetobaccoretailpricetax)

@app.route("/collections/sharewomensmoking")
def sharewomensmoking():
  sharewomensmoking = list(db.sharewomensmoking.find({}, {'_id': False}))
  return jsonify(sharewomensmoking)

@app.route("/collections/smokingdeathsage")
def smokingdeathsage():
  smokingdeathsage = list(db.smokingdeathsage.find({}, {'_id': False}))
  return jsonify(smokingdeathsage)

@app.route("/collections/smokingsecondhanddeaths")
def smokingsecondhanddeaths():
  smokingsecondhanddeaths = list(db.smokingsecondhanddeaths.find({}, {'_id': False}))
  return jsonify(smokingsecondhanddeaths)

@app.route("/collections/supporthelpquittobacco")
def supporthelpquittobacco():
  supporthelpquittobacco = list(db.supporthelpquittobacco.find({}, {'_id': False}))
  return jsonify(supporthelpquittobacco)

@app.route("/collections/taxsharecigprice")
def taxsharecigprice():
  taxsharecigprice = list(db.taxsharecigprice.find({}, {'_id': False}))
  return jsonify(taxsharecigprice)


if __name__ == "__main__":
  app.run()

