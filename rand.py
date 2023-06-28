import random

rf = random.random()*10
print(rf)

print(random.randrange(3, 9))

print(random.randint(3, 9))

mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist, weights = [10, 1, 1], k = 12))

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)


