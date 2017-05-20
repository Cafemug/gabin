def combi(x):
    t=1
    
    for i in range(1,x+1):
        t*=i
    return t





n=int(input())

while(n>0):
    st=input().split(" ")
    st=list(map(int,st))
    a=st[0]
    b=st[1]
    e=b-a
    c=combi(a)
    d=combi(b)
    f=combi(e)
    res=d//(c*f)
    n-=1
    print(res)
