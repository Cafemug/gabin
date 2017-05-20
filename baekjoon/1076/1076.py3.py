def first(x):
    if x=="black":
        return 0
    elif x=="brown":
        return 10
    elif x=="red":
        return 20
    elif x=="orange":
        return 30
    elif x=="yellow":
        return 40
    elif x=="green":
        return 50
    elif x=="blue":
        return 60
    elif x=="violet":
        return 70
    elif x=="grey":
        return 80
    elif x=="white":
        return 90
def second(x):
    if x=="black":
        return 0
    elif x=="brown":
        return 1
    elif x=="red":
        return 2
    elif x=="orange":
        return 3
    elif x=="yellow":
        return 4
    elif x=="green":
        return 5
    elif x=="blue":
        return 6
    elif x=="violet":
        return 7
    elif x=="grey":
        return 8
    elif x=="white":
        return 9
def last(x):
    if x=="black":
        return 1
    elif x=="brown":
        return 10
    elif x=="red":
        return 100
    elif x=="orange":
        return 1000
    elif x=="yellow":
        return 10000
    elif x=="green":
        return 100000
    elif x=="blue":
        return 1000000
    elif x=="violet":
        return 10000000
    elif x=="grey":
        return 100000000
    elif x=="white":
        return 1000000000


a=input()
b=input()
c=input()
d=first(a)
i=second(b)
j=last(c)
res=(i+d)*j
print(res)



    
