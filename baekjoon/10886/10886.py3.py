a=int(input())
countt=0
countn=0
for x in range(a):
    t=int(input())
    if t==0:
        countn+=1
    else:
        countt+=1
if countn>countt:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
