

def ten(x):
    a=x//10
    b=x%10
    count=1
    res=(b*10)+((a+b)%10)
    while True:
        a=res//10
        b=res%10
        if res==x:
            break
        else:
            res=(b*10)+((a+b)%10)
            count+=1
    return count


num=int(input())

print(ten(num))
