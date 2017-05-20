while True:
    i=0
    count=0
    a=input().split()
    a=list(map(int,a))
    if a[0]==-1:
        break
    while True:
        if a[i]==0:
            break
        else:
            i+=1
    for x in range(i):
        for y in range(i):
            if a[y]==2*a[x]:
                count+=1
    print(count)
            
            
                
