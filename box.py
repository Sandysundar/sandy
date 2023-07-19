a='subject'
b='mark'
c='total'
t='tamil'
tm='50'
e='english'
em='65'
m='maths'
mm='99'
s='science'
sm='87'
so='social'
som='78'
x=int(tm)
y=int(em)
z=int(mm)
u=int(sm)
v=int(som)
l=(x+y+z+u+v)
print(type(a))
print(f"╔{'═'*10}╦{'═'*10}╗")
print(f"║{a}{' '*(10-len(a))}║{b}{' '*(10-len(b))}║")
print(f"╠{'═'*10}╬{'═'*10}╣")
print(f"║{t}{' '*(10-len(t))}║{tm}{' '*(10-len(tm))}║")
print(f"║{e}{' '*(10-len(e))}║{em}{' '*(10-len(em))}║")
print(f"║{m}{' '*(10-len(m))}║{mm}{' '*(10-len(mm))}║")
print(f"║{s}{' '*(10-len(s))}║{sm}{' '*(10-len(sm))}║")
print(f"║{so}{' '*(10-len(so))}║{som}{' '*(10-len(som))}║")
print(f"╠{'═'*10}╬{'═'*10}╣")
print(f"║{c}{' '*(10-len(c))}║{l}{' '*(10-len(str(l)))}║")
print(f"╚{'═'*10}╩{'═'*10}╝")

