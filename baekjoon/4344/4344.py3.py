def prin(num):
      print("%.3f"%num,end='')
      print("%")



def sume(x):
    count=0
    x=list(map(int, x))
    sum1=sum(x)-x[0]
    avg=sum1/x[0]
    
    for i in range(1,x[0]+1):
        if x[i]>avg:
            count+=1
            i+=1
        else:
            i+=1
    per=count/x[0]*100
    prin(per)



num=int(input())
for i in range(num):
    temp=input().split()
    sume(temp)
