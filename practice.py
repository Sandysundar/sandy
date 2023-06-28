    #0 1 2 3 4 5 6 7  8  9  10     
a = [1,3,4,5,6,7,9,10,13,15,16]
l = 0
r = len(a)-1
ans = None
data = 15
while(l<=r):
    m = (l+r)//2
    #print(l,m,r)
    if(a[m] == data):
        #print(a[m],m)
        ans = m
        break
    if(a[m]<data):
        l = m+1
    if(a[m]>data):
        r=m-1

    
print(ans)  

