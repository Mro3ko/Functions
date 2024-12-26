def function(number, even):
    result=0
    if even:
        for char in number:
            if int(char)%2==0:
                result+=int(char)

    else:
        for char in number:
            if int(char)%2==1:
                result+=int(char)
    
    return result

print(function("3124",True))
print(function("3124",False))
print(function("20576",False))
print(function("20576",True))
print(function("13115",True))