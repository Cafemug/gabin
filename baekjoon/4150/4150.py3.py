def fib_tail(n):
    def loop(n,first,second):
        if n>1:
            return loop(n-1,second,first+second)
        else :
            return second
    if n==0: return 0
    elif n==1: return 1
    return loop(n,0,1)


def fib_loop(n):
    first=0
    second=1
    
    if n==0: return 0
    elif n==1: return 1

    while n>1:
        n-=1
        temp=first #썜버젼 f=first+second
        first=second# first=second
        second=temp+second#second =f
        
    return second





a=int(input())
print(fib_loop(a))


