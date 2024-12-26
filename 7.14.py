def f(x,y,z):
    if z=="+":
        result=x+y
    elif z=="-":
        result=x-y
    elif z=="*":
        result=x*y
    elif z=="**":
        result=x**y
    elif z=="%":
        result=x%y
    return result

print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))
