def mul(a):
    x=1
    xlist=[]
    count=0
    sum1=0
    alist=[]
    while x<a:
        if a%x==0:
            xlist.append(x)
            x+=1
            count+=1
        else:
            x+=1
    xlist.sort()
    for i in range(count):
        sum1+=xlist[i]
    if sum1==a:
        alist=xlist
    else:
        alist=0
    return alist


while True :
    a=int(input())
    if a==-1:
        break
    alist=mul(a)
  
    if alist!=0:
        x=len(alist)
        print("%d = " %a,end="")
        for i in range(x-1):
            print("%d + "%alist[i],end="") 
        print(alist[x-1])
    else:
        print("%d is NOT perfect."%a)
    
        
