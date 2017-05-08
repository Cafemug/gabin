n=int(input())
a=input().split()
m=int(input())
b=input().split()


a=list(map(int,a))
a=sorted(a)
b=list(map(int,b))


for i in range(m):
    k=0
    mini=0
    maxn=n
    while(mini<=maxn):
        
        mid=(mini+maxn)//2
        
            
        if b[i]<a[mid]:
            maxn=mid-1
        elif b[i]>a[mid]:
            mini=mid+1
        elif b[i]==a[mid]:
            
            k+=1
            print(1)
            break
                
        
    if k==0:
        print(0)
            
       
            
        

