num=input()
num=int(num)

count=0

if num>=100:
    count+=99
    while num>=100:
        
        a=num
        num=str(num)
        num=list(map(int,num))
        if num[0]-num[1]==num[1]-num[2]:
            count+=1
            a-=1
            num=a
        else:
            a-=1
            num=a
        
else:
    count+=num
print(count)
