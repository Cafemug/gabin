i=input().split()
i=list(map(int,i))
sum1=0
for x in range(1,i[0]+1):
    x=x-1
    if x==4 or x==6 or x==9 or x==11: 
        sum1+=30

    elif x==2:
        sum1+=28
    elif x==0:
        sum1+=0
    else:
        sum1+=31
sum1+=i[1]
n=sum1%7
if n==1:
    print("MON")
elif n==2:
    print("TUE")
elif n==3:
    print("WED")
elif n==4:
    print("THU")
elif n==5:
    print("FRI")
elif n==6:
    print("SAT")
else:
    print("SUN")
