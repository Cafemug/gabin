a,b=(input().split())
c=input().split()

a=int(a)
b=int(b)
i=0

c=list(map(int,c))

while i<a:
    if c[i]<b:
        print(c[i],end=' ')
        i+=1
    else:
        i+=1
    
