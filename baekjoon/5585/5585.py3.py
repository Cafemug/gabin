a=int(input())
b=1000-a
count=0
while b!=0:
    if b>=500:
        count+=1
        b-=500
    elif b>=100:
        c=b//100
        count+=c
        b-=(c*100)
    elif b>=50:
        count+=1
        b-=50
    elif b>=10:
        d=b//10
        b-=(d*10)
        count+=d
    elif b>=5:
        count+=1
        b-=5
    else:
        f=b//1
        b-=f
        count+=f
print(count)
