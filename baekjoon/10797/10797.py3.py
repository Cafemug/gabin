a=int(input())
ulist=input()
ulist=ulist.split()
ulist=list(map(int,ulist))
count=0
for x in range(5):
    t=ulist[x]%10
    if t==a:
        count+=1
print(count)
