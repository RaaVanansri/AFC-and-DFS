import random
import requests
import pymongo
import os

from dotenv import load_dotenv

load_dotenv()

dbstring = os.getenv('DBCONSTR')
client = pymongo.MongoClient(dbstring)

db = client["AFC"]
afcdb = db["sample"]

#Activating the channel if it's not reserved by incumbents

def afcmain(band,chno):
    bandinfo = afcdb.find({"_id":band})
    s = ''
    for i in bandinfo:
        if i['_id'] == band and i[str(chno)]["Status"] == 'Inactive': #i['1']['Status'] __pydevd_ret_val_dict['Cursor.next']['_id'] j['1']['Status']
            afcdb.update_one({'_id':band},{"$set":{f"{chno}.Status":"Active"}}, upsert=True)
            print(f"Selected Channel {chno} is available to transmit data")
        else:
            s=f'Selected Channel {chno} is not available to transmit to data at this moment.These are available channels'
            for j in i.items():
                if j[0] == "_id":
                    pass
                elif j[1]['Status'] == "Inactive":
                    s += f"Channel {j[0]} with{j[1]['Band']} \n"
        return s


print(afcmain("UNI5",83))