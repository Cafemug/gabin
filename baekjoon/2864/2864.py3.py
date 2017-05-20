def mini(a,b):
    alist=[]
    blist=[]
    suma=str()
    sumb=str()
    for i in str(a):
       
        if i==str(6):
            i=str(5)
        alist.append(i)
    for i in str(b):
        if i==str(6):
            i=str(5)
        blist.append(i)
    x=len(alist)
    y=len(blist)
    for i  in range(x):
        suma+=alist[i]
    for i  in range(y):
        sumb+=blist[i]
    n=int(suma)
    m=int(sumb)
    sum2=n+m
    return sum2
        
def many(a,b):
    alist=[]
    blist=[]
    suma=str()
    sumb=str()
    for i in str(a):
       
        if i==str(5):
            i=str(6)
        alist.append(i)
    for i in str(b):
        if i==str(5):
            i=str(6)
        blist.append(i)
    x=len(alist)
    y=len(blist)
    for i  in range(x):
        suma+=alist[i]
    for i  in range(y):
        sumb+=blist[i]
    n=int(suma)
    m=int(sumb)
    sum2=n+m
    return sum2


a,b=input().split()
print(mini(a,b) , many(a,b))

