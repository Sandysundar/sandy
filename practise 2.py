#mcq questions:

##a=input(f"1.what is your name \n a.sundar\n b.sandy \n c.python")
##answer=input("ans: ")
##if answer==a:
##    print("correct answer")
##print("1")
##else:
##    print("wrong answer")

mcq=[
{"q":"what is your name?","o":['a.sundar','b.sandy','c.python'],"a":'sundar'},
{"q":"what is your age?","o":[a.23,b 24,c.30],"a":23},
{"q":"who is the founder of python?","o":['a. jay','b. sandy','srinath'],"a":'sandy'}, ]

for i in mcq:
    print (i['q'])
    for x in i['o']:
        print(" ",x)

    ans=input("enter the answer")
    if i['a']==ans:
        print("correct")
    else:
        print("wrong")


    print()
