import pymongo
client = pymongo.MongoClient("mongodb://raavanan:Sr1kutty77@cluster0-shard-00-00.z89ji.mongodb.net:27017,cluster0-shard-00-01.z89ji.mongodb.net:27017,cluster0-shard-00-02.z89ji.mongodb.net:27017/Channel?ssl=true&replicaSet=atlas-5yhivq-shard-0&authSource=admin&retryWrites=true&w=majority")

dict = {}
db = client["AFC"]
afcdb = db["sample"]
for i in afcdb.find():
    a = (i)
    print(a)
    dict.update(a)


x=int(input('Available MHz\n 20\n 40\n 80\n 160\n Enter your choice:'))
# 20 mhz
if x==20:
    b=dict
    print('Available Channels')
    chl= [i for i in b if b[i]=='inactive']
    [print(i) for i in chl]
    channel=int(input('Choose channel:'))
    print(f'Channel {channel} is set for transmit')
"""
afcdb.insert_one({
    str(channel):'active'
})

afcdb.delete_many({
    str(channel):'inactive'
})"""