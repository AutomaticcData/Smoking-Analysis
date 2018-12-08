# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:26:54 2018
UCI Team Project #2
@author: anthonyalvarez
"""


# coding: utf-8

#   -----------REFERENCES-----------------------------------------------------------------------
# * https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# * https://github.com/AutomaticcData/UCI-Eats/blob/master/UCI%20Eats%20-%20Team%20One.ipynb
# * https://stackoverflow.com/questions/10037742/replace-part-of-a-string-in-python
# * https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
# * https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
# * https://stackoverflow.com/questions/27416296/how-to-push-a-csv-data-to-mongodb-using-python
# * https://www.quora.com/How-can-I-import-a-CSV-file-data-to-MongoDB-using-Python-Flask
# * https://stackoverflow.com/questions/27416296/how-to-push-a-csv-data-to-mongodb-using-python
# * https://stackoverflow.com/questions/39267614/csv-file-does-not-exist-pandas-dataframe
# * https://stackoverflow.com/questions/177287/alert-boxes-in-python
# 
# 

# --------------IMPORT DEPENDENCIES
import os
#import json
import pymongo
import pandas as pd
#from collections import defaultdict
#import win32api (commented out for my mac)


# Switch True/False to tell script whether you want to save the data as a json or not
blnsavejson = False


# --------------CONNECT TO MONGODB
# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance
client = pymongo.MongoClient(conn)

# Drop database if exists
client.drop_database('smoking')

#create a database
db = client.smoking
# ---

#create a listing of objects in the data directory
this_dir = os.listdir("data")

#store the number of datasets found to compare later
#len(this_dir)
numfiles = len(this_dir)



#setup a counter
row = 0

for i in this_dir:
    row += 1
    file_name = i.replace(".csv","")
    #print(file_name)    
    #---------------------------
    dataname = 'data/' + file_name + '.csv'
    jsonname = 'json/' + file_name + '.json'

    if file_name == 'average-price-of-a-pack-of-cigarettes':
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.avgpricepack.drop()                                 #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.avgpricepack.insert_many(obj_records)        
        
        print(f'{row} avgpricepack')
        
    elif file_name == 'comparing-the-share-of-men-and-women-who-are-smoking':
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.comparemenwomensmoking.drop()                       #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.comparemenwomensmoking.insert_many(obj_records)  
        print(f'{row} comparemenwomensmoking')
        
    elif file_name == 'consumption-per-smoker-per-day':
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.consumepersmokerperday.drop()                       #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.consumepersmokerperday.insert_many(obj_records)  
        print(f'{row} consumepersmokerperday')
        
    elif file_name == 'consumption-per-smoker-per-day-bounds': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.consumepersmokerperdaybounds.drop()                 #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.consumepersmokerperdaybounds.insert_many(obj_records)  
        print(f'{row} consumepersmokerperdaybounds')
  
    elif file_name == 'daily-smoking-prevalence-bounds': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.dailysmokingprevbounds.drop()                       #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.dailysmokingprevbounds.insert_many(obj_records)  
        print(f'{row} dailysmokingprevbounds')
        
    elif file_name == 'enforcement-of-bans-on-tobacco-advertising': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.enforcebanstobacad.drop()                           #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.enforcebanstobacad.insert_many(obj_records)  
        print(f'{row} enforcebanstobacad')
        
    elif file_name == 'number-of-deaths-from-secondhand-smoke': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.numdeathssecondhand.drop()                          #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.numdeathssecondhand.insert_many(obj_records)  
        print(f'{row} numdeathssecondhand')
        
    elif file_name == 'number-of-deaths-from-tobacco-smoking': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.numdeathstobaccosmoking.drop()                      #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.numdeathstobaccosmoking.insert_many(obj_records)  
        print(f'{row} numdeathstobaccosmoking')
        
    elif file_name == 'number-of-total-daily-smokers': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.numtotaldailysmokers.drop()                         #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.numtotaldailysmokers.insert_many(obj_records)  
        print(f'{row} numtotaldailysmokers')
        
    elif file_name == 'sales-of-cigarettes-per-adult-per-day': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.salesofcigsperadultperday.drop()                    #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.salesofcigsperadultperday.insert_many(obj_records)  
        print(f'{row} salesofcigsperadultperday')
        
    elif file_name == 'secondhand-smoke-deaths-by-age': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.secondhandsmokedeathsbyage.drop()                   #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.secondhandsmokedeathsbyage.insert_many(obj_records)  
        print(f'{row} secondhandsmokedeathsbyage')
        
    elif file_name == 'share-of-cancer-deaths-attributed-to-tobacco': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.sharecancerdeathsfromtobacco.drop()                 #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.sharecancerdeathsfromtobacco.insert_many(obj_records)  
        print(f'{row} sharecancerdeathsfromtobacco')
        
    elif file_name == 'share-of-men-who-are-smoking-by-level-of-prosperity': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.sharemensmokinglevelprosperity.drop()               #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.sharemensmokinglevelprosperity.insert_many(obj_records)  
        print(f'{row} sharemensmokinglevelprosperity')
        
    elif file_name == 'share-of-men-who-are-smoking': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.sharemensmoking.drop()                              #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.sharemensmoking.insert_many(obj_records)  
        print(f'{row} sharemensmoking')
        
    elif file_name == 'share-of-tobacco-retail-price-that-is-tax': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.sharetobaccoretailpricetax.drop()                   #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.sharetobaccoretailpricetax.insert_many(obj_records)  
        print(f'{row} sharetobaccoretailpricetax')
        
    elif file_name == 'share-of-women-who-are-smoking': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.sharewomensmoking.drop()                            #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.sharewomensmoking.insert_many(obj_records)  
        print(f'{row} sharewomensmoking')
        
    elif file_name == 'smoking-and-secondhand-deaths': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.smokingsecondhanddeaths.drop()                      #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.smokingsecondhanddeaths.insert_many(obj_records)  
        print(f'{row} smokingsecondhanddeaths')
        
    elif file_name == 'smoking-deaths-by-age': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.smokingdeathsage.drop()                             #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.smokingdeathsage.insert_many(obj_records)  
        print(f'{row} smokingdeathsage')
        
    elif file_name == 'support-to-help-to-quit-tobacco-use': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.supporthelpquittobacco.drop()                       #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.supporthelpquittobacco.insert_many(obj_records)  
        print(f'{row} supporthelpquittobacco')
        
    elif file_name == 'taxes-as-share-of-cigarette-price': 
        #---------------------------
        mt_df = pd.read_csv(dataname,encoding = 'ISO-8859-1')  #load csv
        #---------------------------
        db.taxsharecigprice.drop()                             #drop remove duplicates
        
        if blnsavejson: mt_df.to_json(jsonname)                #save json file
        
        obj_records = mt_df.to_dict(orient = 'records')
        db.taxsharecigprice.insert_many(obj_records)  
        print(f'{row} taxsharecigprice')

    else:
        print(f'{row} - NOTHING TO DO')
    

#win32api.MessageBox(0, 'Import MongoDB Script has completed', 'Attention!', 0x00001000) 
