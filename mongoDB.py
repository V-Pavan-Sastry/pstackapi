from pymongo import MongoClient
from bson import ObjectId, SON
# Replace the following variables with your actual MongoDB connection details
MONGO_URL = "mongodb+srv://pavanv180402:WR5i0KVUcBf6yL9n@cluster0.q3lamrv.mongodb.net/"
def readDB():
    client = MongoClient(MONGO_URL)
    database = client["vp121"]
    collection = database["vp"]
    print(collection)
    documents = collection.find({})
    print(documents)
    docs={}
    docs['PROCESS_STACK']=[]
    # Print the fetched documents
    for document in documents[0]['PROCESS_STACK']:
        print("Document:", document)
        docs['PROCESS_STACK'].append(document)
    return docs

def addBiscs2DB(val:bool):
    client = MongoClient(MONGO_URL)
    database = client["vp121"]
    collection = database["vp"]
    print(collection)
    oid = ObjectId('65fef6d998837ac680b9d882')
    update_op = SON([("$push", {"PROCESS_STACK": val})])
    result = collection.update_one({'_id': oid}, update_op)
    if result.modified_count > 0:
        msg="Successfully added a value to the array"
    else:
        msg="Failed to add a  value to the array"
    return {"message": msg}
 

def remBisc4mDB():
    client = MongoClient(MONGO_URL)
    database = client["vp121"]
    collection = database["vp"]
    print(collection)
    oid = ObjectId('65fef6d998837ac680b9d882')
    update_op ={'$pop': {'PROCESS_STACK': -1}}
    result = collection.update_one({'_id': oid}, update_op)
    if result.modified_count > 0:
        msg="Successfully removed a value to the array"
    else:
        msg="Failed to remove a  value to the array"
    return {"message": msg}
#readDB()
#addBiscs2DB(val=True)
#readDB()
#addBiscs2DB(val=False)
#readDB()