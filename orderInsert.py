from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") #host uri
db = client.mymongodb    #Select the database
myorder = db.order #Select the collection name

def orderInsRecord(x,y,z,a):
    print('insertRecord')
    mydict = {"name": x, "address": y ,"item" : z, "date" : a}
    x = myorder.insert_one(mydict)

def orderlistRecords():
    x = myorder.find({})
    orderItem = []
    for obj in x:
        print(obj)
        orderItem.append(obj)
    return orderItem

if __name__ == "__main__":
    orderlistRecords()


