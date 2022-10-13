def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def intdiv(a,b):
    return a//b
def power(a,b):
    return a**b
def roundnum(a):
    a = a+(-0.5 if a<0 else 0.5)
    x = str(a)
    y = x.find('.')
    return x[0:y]
def ceil(a):
    a = a+0.5
    return int(a)
def floor(a):
    a = a-0.5
    return int(a)
def sqroot(a):
    return a**0.5
def squrenum(a):
    return a**2
n = 7
a = 4.9
b = 3
if n==1:
    print(add(a,b))
elif n==2:
    print(sub(a,b))
elif n==3:
    print(multiply(a,b))
elif n==4:
    print(division(a,b))
elif n==5:
    print(intdiv(a,b))
elif n==6:
    print(power(a,b))
elif n==7:
    print(roundnum(a))
elif n==8:
    print(ceil(a))
elif n==9:
    print(floor(a))
elif n==10:
    print(sqroot(a))
elif n==11:
    print(squrenum(a))
