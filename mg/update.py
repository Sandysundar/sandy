from db import uc


##data = ["sandy","python","flutter","java","html","jay","srinath","thamizh"]
##for i in data:
##    uc.insert_one({"username":i,'age':10+len(i)})
    
#uc.insert_one({"username":"html",'age':15,"skills":['front-end']})

##data = list(uc.find({"age":20}).sort("username").limit(3))
##print(len(data))
##print(list(data))
##for i in data:
##    print(f"{i['username']},{i['age']}")


#uc.update_one({"username":"jayakumar"},{"$set":{"username":"jay","email":"jay@gmail.com"}})

#uc.delete_one({"username":"jay"})
#uc.delete_many({})
