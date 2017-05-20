num=int(input())
temp=int(input())
count=0

for i in range(num):
    count+=temp%10
    temp=temp//10

print(count)
