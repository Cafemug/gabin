
a=int(input())

for i in range(a):
    x=i
    print('',end=''.rjust(x))   
    for x in range(a):
        print("*",end='')

    a-=1
    print()
