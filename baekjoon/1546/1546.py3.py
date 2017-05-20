def conv(x):
    return x/large*100


n=int(input())
scores=input().split()
scores =list(map(int,scores))
large=max(scores)
scores=list(map(conv,scores))

avg=sum(scores)/n
print("%.2f"%avg)
