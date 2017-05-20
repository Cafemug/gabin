a=int(input())
count=1
res=0
for i in range(1,a+1):
    count*=i
count=str(count)
x=count[::-1]
for i in str(x):
    if i=='0':
        res+=1
    else:
        print(res)
        break
