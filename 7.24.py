def function(expresion):
    result=int(expresion[0])
    for i in range (1,len(expresion),2):
        if expresion[i]=="-":
            result-=int(expresion[i+1])
        elif expresion[i]=="+":
            result+=int(expresion[i+1])
    return result

print(function("2+3"))
print(function("3+8+1"))
print(function("2+3-4+5-0"))
