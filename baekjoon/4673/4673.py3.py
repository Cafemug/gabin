num=0
x=0
nlist=[]
tlist=[]
while  num<=10001:
    sum1=0
    num=str(num)
    a=int(num)
    num=list(map(int,num))
    lens=len(num)
    for x in range(lens):
        sum1+=num[x]
    sum1+=a
    nlist.append(sum1)
    nlist.sort()
    lenn=len(nlist)
    num=a
    num+=1


def search(nlist , lenn,x):
    first=0
    last=lenn-1
    while first<=last:
        mid=(first+last)//2
        if x==nlist[mid]:
            return mid
        else:
            if x<nlist[mid]:
                last=mid-1
            else:
                first=mid+1
    return -1;

print(1)
print(3)
while x<=10000:
    idx=search(nlist,lenn,x)
    if idx==-1:
        print(x)
        x+=1
    else:
        x+=1
    
      
    
