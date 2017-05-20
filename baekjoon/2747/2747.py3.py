def fibonacci(number, a=1, b=0):
    for _ in range(number + 1):
        a, b = b, a + b

    return a



n = int(input())


print(fibonacci(n))