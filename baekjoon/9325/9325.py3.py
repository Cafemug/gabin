t=int(input())
for i in range(t):
    s=int(input())
    n=int(input())
    for x in range(n):
        q,p=input().split()
        q=int(q)
        p=int(p)
        temp=q*p
        s+=temp
    print(s) 
    
