a=int(input())
total=1
tot=1
for x in range(1,a+1):
    total*=x
for x in range(1,a-4+1):
    tot*=x
reg=total//(24*tot)
print(reg)
