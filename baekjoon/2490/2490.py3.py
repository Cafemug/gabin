alist=input().split()
tlist=input().split()
vlist=input().split()

count1=0
count2=0
count3=0

for i in range(4):
    if alist[i]=='1':
        count1+=1


for i in range(4):
    if tlist[i]=='1':
        count2+=1


for i in range(4):
    if vlist[i]=='1':
        count3+=1

if count1==0:
    print('D')
elif count1==1:
    print('C')
elif count1==2:
    print('B')
elif count1==3:
    print('A')
elif count1==4:
    print('E')

if count2==0:
    print('D')
elif count2==1:
    print('C')
elif count2==2:
    print('B')
elif count2==3:
    print('A')
elif count2==4:
    print('E')

if count3==0:
    print('D')
elif count3==1:
    print('C')
elif count3==2:
    print('B')
elif count3==3:
    print('A')
elif count3==4:
    print('E')
