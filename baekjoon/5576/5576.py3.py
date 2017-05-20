flist=[]
llist=[]
a=0
while a<10:
    x=int(input())
    flist.append(x)
    a+=1

a=0
while a<10:
    d=int(input())
    llist.append(d)
    a+=1

def merge(left,right):
    olist=[]
    while left!=[] and right !=[]:
        if left[0]>right[0]:
            olist+=[right[0]]
            right.remove(right[0])
        else:
            olist+=[left[0]]
            left.remove(left[0])
    if left==[]:
        return olist+right
    else:
        return olist+left


def divide(lists):
    cnt=len(lists)
    mid=cnt//2
    left=lists[:mid]
    right=lists[mid:]
    if cnt >2:
        
        return merge(divide(left),divide(right))
    else:
        
        return merge(left,right)

n=divide(flist)
m=divide(llist)

res1=n[7]+n[8]+n[9]
res2=m[7]+m[8]+m[9]

print(res1 ,res2)

    
