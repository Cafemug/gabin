a=int(input())
alist=input().split()
x=len(alist)
alist=list(map(int,alist))
alist.sort()
res=alist[0]*alist[x-1]
print(res)
