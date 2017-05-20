a=input()
a=int(a)
i=0
while a>i:
    string=input()
    n,_,b=string.partition(' ')
    b=list(b)
    
    w=len(b)
    for x in range(w):
        j=0
        n=int(n)
        while n>j:
            print(b[x],end='')
            j+=1
    print()
    i+=1
