from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")

db = client.sandy

uc = db.User


#col.insert_one({"username":"thamizh","age":21,"skills":["driving","developer"]})
#infoCol.insert_one({"date":"28-02-2023",})

##users = [
##    {"username":"python","age":20,"skills":["driving","developer"]},
##    {"username":"java","age":21,"skills":["driving","developer"]},
##    {"username":"C++","age":25,"skills":["driving","developer"]}  
##    ]
##col.insert_many(users)



##data = col.find({"age":21})
##print(list(data))
##for i in list(data):
##    print(i["username"])

##d = col.find_one({"age":20})
##print(d)




