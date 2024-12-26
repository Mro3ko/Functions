def function(code):
    sum=0
    for char in code[:3]:
        sum+=int(char)
    return int(code[3])==sum%7

print(function("1082"))
print(function("2035"))
print(function("1114"))
print(function("7071"))
