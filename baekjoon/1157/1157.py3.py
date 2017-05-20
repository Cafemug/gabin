a=input()

a=a.upper()
a=sorted(a)
count=[]
count1=1
alist=[]
lens=len(a)
i=0
while i<lens:
    i+=count1-1
    
    count1=0
    if i>=lens:
        break
    
    for j in range(lens):
        if a[i]==a[j]:
            count1+=1
    
    count.append(((a[i]),count1))

    i+=1;   
lens2=len(count)
for k in range(lens2):
    alist.append(count[k][1])
m=max(alist)
k=alist.count(m)
if k==1:
    for u in range(lens2):
        if count[u][1]==m:
            print(count[u][0])
else:
    print('?')
                 

