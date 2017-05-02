    

def fibo1(n):
    def loop(n,first,second):
        if n==0: return 0
        elif n==1: return second
        elif n>=2:
            return loop(n-1,second,first+second)

    return loop(n,0,1)

def fibo0(n):
    def loop(n,first,second):
        if n==0: return 1
        elif n==1: return second
        elif n>=2:
            return loop(n-1,second,first+second)

    return loop(n,1,0)


a=int(input())
for i in range(a):
    x=int(input())
    print(fibo0(x),end=" ")
    print(fibo1(x))

    

