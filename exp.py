
#exception handling


try:
    age = 100
    if(age>100):
        raise Exception("age should be leesthen 100")
    print(age)
except Exception as e:
    print("somthing went wrong",e)
else:
    print('we have no error')
finally:
    print("trying completed")







print(10+20)
