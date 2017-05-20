a=int(input())
for i in range(a):
    
    x=a-i
    print('',end=''.rjust(x-1))
    while(x<=a):
        print('*',end='')
        x+=1
    print()


