class Tel():
    
    def __init__(self,mic=1,display=1.5):
        self.mic = mic
        self.display = display
        self.__dailpad = True

    def makeCall(self,number):
        print(f"calling {number}...")
        
class CellPhone(Tel):
    
    def __init__(self,keypad=True):
        self.keypad = keypad
        self.contact = []
        super().__init__()

    def addContact(self,name):
        self.contact.append(name)

    def makeCall(self,name):
        inu = True
        for i in name:
            if(i.isnumeric() or i=="+" or i == " "):
                inu = True
            else:
                inu = False
                break
                
        if(name in self.contact):
            print(f'calling {name}☺...')
        elif(inu):
            print(f"calling {name}...!")
        else:
            print("Invalid contact")
        
    
class Test():
    pass

lava = CellPhone()

print(lava.keypad)
lava.makeCall("88888")
print(lava.mic)
#print(lava.__dailpad)
lava.addContact("sundar")
lava.addContact("jay")
lava.addContact("srinath")
print(lava.contact)
lava.makeCall("jay")


for i in range(5):
    if(i == 2):
        continue
    print(i)
