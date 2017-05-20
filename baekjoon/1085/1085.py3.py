alist=input().split()
alist=list(map(int,alist))
x=alist[2]-alist[0]
y=alist[3]-alist[1]
i=alist[0]
j=alist[1]
ulist={x,y,i,j}
print(min(ulist))
