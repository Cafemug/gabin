a=int(input())
alist=[]
for x in range(a):
    n=input()
    alist.append(n)
alist=list(map(int,alist))
alist.sort()

for i in range(a):
    print(alist[i])
