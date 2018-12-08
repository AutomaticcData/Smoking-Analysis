import pymongo
from flask import Flask, jsonify, render_template

app = Flask(__name__)
conn = "mongodb://localhost:27017"

client = pymongo.MongoClient(conn)
db = client.smoking

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/data")
def welcome():
    html =        '<!DOCTYPE html>																																									  '
    html = html + '<html lang="en-us">																																								  '
    html = html + '<head>																																											  '
    html = html + '  <meta charset="UTF-8">																																							  '
    html = html + '    <title>Smoking Hot Data</title>																																				  '
    html = html + '    <style type="text/css">																																						  '
    html = html + '            p {																																									  '
    html = html + '                font-size: 20px;																																					  '
    html = html + '            }																																									  '
    html = html + '            li {																																									  '
    html = html + '                font-size: 15px;																																					  '
    html = html + '            }																																									  '
    html = html + '            h1 {																																									  '
    html = html + '                background-color: black;																																			  '
    html = html + '                color: yellow;																																					  '
    html = html + '            }																																									  '
    html = html + '            .shadow{																																								  '
    html = html + '                box-shadow: 5px 10px #888888;																																	  '
    html = html + '            }																																									  '
    html = html + '            .sectionback{																																						  '
    html = html + '                background-color: tomato;																																		  '
    html = html + '            }																																									  '
    html = html + '            .font2{																																								  '
    html = html + '                font-size: 12px																																					  '
    html = html + '            }																																									  '
    html = html + '            .whiteback{																																							  '
    html = html + '                background-color: whitesmoke;																																	  '
    html = html + '                color: black;																																					  '
    html = html + '            }																																									  '
    html = html + '																																													  '
    html = html + '            ul {																																									  '
    html = html + '                border: 1px solid whitesmoke;																																	  '
    html = html + '                }																																								  '
    html = html + '    </style>																																										  '
    html = html + '</head>																																											  '
    html = html + '<body background="https://www.aidsmap.com/v636227698080200000/file/1213214/Smoking.png" alt="An image with a lit cigarette that is crossed out.">																																			  '
    html = html + '<h1>Smoking Data Project</h1>																																		  '
    html = html + '<h3>Welcome to our Smoking Data Depot</h3>																																	  '
    html = html + '<img class="shadow" src="https://www.spineuniverse.com/sites/default/files/imagecache/gallery-large/wysiwyg_imageupload/3998/2017/10/10/cigarettes_stacked_-1642232_1920.jpg" height="100" width="200" alt="Cigarettes that are stacked upon one another."/>																										  '
    html = html + '<section>																																										  '
    html = html + '    <div id="7" width="200"><p class="border1 whiteback shadow">Available Routes</p></div>																						  '
    html = html + '	<ul class="shadow">																																								  '
    html = html + '		<li><a href="http://localhost:5000/frontgate" target="_blank">Smoking Collections Listing</a></li>																	  '

    html = html + '	<hr>		'

    html = html + '        <li><a href="http://localhost:5000/collections/avgpricepack" target="_blank">average-price-of-a-pack-of-cigarettes</a></li>                 							'                 
    html = html + '        <li><a href="http://localhost:5000/collections/comparemenwomensmoking" target="_blank">comparing-the-share-of-men-and-women-who-are-smoking</a></li>                 '
    html = html + '        <li><a href="http://localhost:5000/collections/consumepersmokerperday" target="_blank">consumption-per-smoker-per-day</a></li>                                       '
    html = html + '        <li><a href="http://localhost:5000/collections/consumepersmokerperdaybounds" target="_blank">consumption-per-smoker-per-day-bounds</a></li>                          '
    html = html + '        <li><a href="http://localhost:5000/collections/dailysmokingprevbounds" target="_blank">daily-smoking-prevalence-bounds</a></li>                                      '
    html = html + '        <li><a href="http://localhost:5000/collections/enforcebanstobacad" target="_blank">enforcement-of-bans-on-tobacco-advertising</a></li>                               '
    html = html + '        <li><a href="http://localhost:5000/collections/numdeathssecondhand" target="_blank">number-of-deaths-from-secondhand-smoke</a></li>                                  '
    html = html + '        <li><a href="http://localhost:5000/collections/numdeathstobaccosmoking" target="_blank">number-of-deaths-from-tobacco-smoking</a></li>                               '
    html = html + '        <li><a href="http://localhost:5000/collections/numtotaldailysmokers" target="_blank">number-of-total-daily-smokers</a></li>                                          '
    html = html + '        <li><a href="http://localhost:5000/collections/salesofcigsperadultperday" target="_blank">sales-of-cigarettes-per-adult-per-day</a></li>                             '
    html = html + '        <li><a href="http://localhost:5000/collections/secondhandsmokedeathsbyage" target="_blank">secondhand-smoke-deaths-by-age</a></li>                                   '
    html = html + '        <li><a href="http://localhost:5000/collections/sharecancerdeathsfromtobacco" target="_blank">share-of-cancer-deaths-attributed-to-tobacco</a></li>                   '
    html = html + '        <li><a href="http://localhost:5000/collections/sharemensmoking" target="_blank">share-of-men-who-are-smoking</a></li>                                                '
    html = html + '        <li><a href="http://localhost:5000/collections/sharemensmokinglevelprosperity" target="_blank">share-of-men-who-are-smoking-by-level-of-prosperity</a></li>          '
    html = html + '        <li><a href="http://localhost:5000/collections/sharetobaccoretailpricetax" target="_blank">share-of-tobacco-retail-price-that-is-tax</a></li>                        '
    html = html + '        <li><a href="http://localhost:5000/collections/sharewomensmoking" target="_blank">share-of-women-who-are-smoking</a></li>                                            '
    html = html + '        <li><a href="http://localhost:5000/collections/smokingdeathsage" target="_blank">smoking-and-secondhand-deaths</a></li>                                              '
    html = html + '        <li><a href="http://localhost:5000/collections/smokingsecondhanddeaths" target="_blank">smoking-deaths-by-age</a></li>                                               '
    html = html + '        <li><a href="http://localhost:5000/collections/supporthelpquittobacco" target="_blank">support-to-help-to-quit-tobacco-use</a></li>                                  '
    html = html + '        <li><a href="http://localhost:5000/collections/taxsharecigprice" target="_blank">taxes-as-share-of-cigarette-price</a></li>											'

    html = html + '    </ul>																																										  '
    html = html + '</section>																																										  '
    html = html + '</body>																																											  '
    html = html + '</html>																																											  '

    return html




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

@app.route("/frontgate/")
def maingate():
    tablenames = []
    collections = db.list_collection_names()
    for collection in collections:
      tablenames.append(collection)
    # sort the list
    tablenames = sorted(tablenames)
    objcoll = {"CollectionName": tablenames}
    return jsonify(objcoll)

if __name__ == "__main__":
  app.run()

