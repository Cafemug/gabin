


alist=[]
tlist=[]
for i in range(8):
    x=input()
    alist.append(x)
alist=list(map(int,alist))
ulist=sorted(alist)
res=ulist[3]+ulist[4]+ulist[5]+ulist[6]+ulist[7]
print(res)
for i in range(5):
    t=ulist[i+3]
    x=alist.index(t)
    tlist.append(x+1)
slist=sorted(tlist)
for i in range(5):
    print(slist[i],end=' ')
