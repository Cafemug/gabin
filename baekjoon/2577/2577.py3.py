a=int(input())
b=int(input())
c=int(input())
alist=str(a*b*c)
tlist=[0,0,0,0,0,0,0,0,0,0]
alist.split()
x=len(alist)
alist=list(map(int,alist))


for i in range(x):
    for j in range(10):
        if alist[i]==j:
            tlist[j]+=1

for x in range(10):
    print(tlist[x])
