a=int(input())

d=(a//5)-1
b=a-(5*d)
c=b//3
e=a//5
f=a-(e*5)
g=f//3
x=e-2
y=a-(x*5)
z=y//3
if(a==4 or a<3 or a==7):
    print(-1)
elif (a%5==4 or a%5==1):
    print(c+d)
elif (a%5==0 or a%5==3):
    print(e+g)
elif (a%5==2):
    print(x+z)
else:
    print(-1)

