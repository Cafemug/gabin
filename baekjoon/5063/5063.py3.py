a=int(input())
for i in range(a):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    d=a+c
    if d>b:
        print("do not advertise")
    elif d==b:
        print("does not matter")
    else:
        print("advertise")
