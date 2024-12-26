def Fibonacci(n):
    a=0
    b=1
    if n==1:
        return a
    elif n==2:
        return b
    elif n>2:
        for i in range(n-2):
            c=a+b
            a,b=b,c
    return c
for i in range(1,20):
    print(Fibonacci(i))
