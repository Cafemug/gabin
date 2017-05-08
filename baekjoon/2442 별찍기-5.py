a=int(input())

for x in range(a):
    b=a-x-2
    x=2*x+1
    while b>=0:
        print(" ",end='')
        b-=1
    for i in range(x):
        
        print("*",end='')
    print("")
        
