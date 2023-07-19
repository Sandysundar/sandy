string="sundar"

print(string[0])

#price of products:
milk=50
biscuit=100
choclate=150
stock=25
sales=input("enter the product")
if sales=='milk':
    quantity=int(input("enter the quantity"))
    if quantity <= stock:
        price=quantity*milk
        print("available ")
        print("your total amount is : ",price)
        
    else:
        print("out of stock")
elif sales=="biscuit":
    quantity=int(input("enter the quantity"))
    if quantity <= stock:
        price=quantity*biscuit
        print("available ")
        print("your total amount is : ",price)
        
elif sales=="choclate":
    quantity=int(input("enter the quantity"))
    if quantity <= stock:
        price=quantity*choclate
        print("available ")
        print("your total amount is : ",price)
else:
    print("not available or out of stock")















    
