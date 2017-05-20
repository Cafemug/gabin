n=int(input())
for i in range(1,n+1):
    a=input().split()
    a=list(map(int,a))
    print("Case #"+str(i)+": "+str(a[0]+a[1]))
    
