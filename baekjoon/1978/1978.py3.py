a=int(input())
alist=input().split()
count1=0
alist=list(map(int,alist))
for x in range(a):
    count2=0
    for i in range(1,alist[x]+1):
        if alist[x]%i==0:
            count2+=1

    if count2==2:
        count1+=1
print(count1)
