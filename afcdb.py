import random
import requests
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

dbstring = os.getenv('DBCONSTR')
client = pymongo.MongoClient(dbstring)

def dbcollection():

    def uniband():

        unibandlist = [[[1,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,65,59,73,77,81,85,89,93],[3,11,19,27,35,43,51,59,67,75,83,91],[7,23,39,55,71,87],[15,47,79]],
        [[97,101,105,109,113],[99,107,115],[103,119],[111]],
        [[117,121,125,129,133,137,141,145,149,153,157,161,165,169,173,177,181],[123,131,139,147,155,163,171,179],[135,151,167],[143]],
        [[185,189,193,197,201,205,209,213,217,221,225,225,233],[187,195,203,211,219,227],[183,199,215],[175,207]]]

        y = {}
        for i,j in enumerate(band):
            freq = frequency
            for k in j:
                avail = random.randint(0,1)
                if i == 0:y.update({f'{k}':{"Band":"20Mhz","Frequency(Mhz)":f'{freq}-{freq+20}',"Status":"Active" if avail == 1 else "Inactive"}});freq += 20
                elif i == 1:y.update({f'{k}':{f"Band":"40Mhz","Frequency(Mhz)":f'{freq}-{freq+40}',"Status":"Active" if avail == 1 else "Inactive"}});freq += 40
                elif i == 2:y.update({f'{k}':{f"Band":"80Mhz","Frequency(Mhz)":f'{freq}-{freq+80}',"Status":"Active" if avail == 1 else "Inactive"}});freq += 80
                elif i == 3:y.update({f'{k}':{f"Band":"160Mhz","Frequency(Mhz)":f'{freq}-{freq+160}',"Status":"Active" if avail == 1 else "Inactive"}});freq += 160
        
        return y
    
    db = client["AFC"]
    afcdb = db["sample"]
    
    
    afcdb.update_one({'_id':"UNI5"},{"$set":uniband(unibandlist[0],5945)},upsert=True)
    afcdb.update_one({'_id':"UNI6"},{"$set":uniband(unibandlist[1],6425)},upsert=True)
    afcdb.update_one({'_id':"UNI7"},{"$set":uniband(unibandlist[2],6525)},upsert=True)
    afcdb.update_one({'_id':"UNI8"},{"$set":uniband(unibandlist[3],6885)},upsert=True)


