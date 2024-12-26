def function(number):
    number_text=str(number)
    suma=0
    for i in "0123456789":
        count=number_text.count(i)
        if count>1:
            suma+=int(i)*count
        
    return suma

print(function(1027))
print(function(2303357))
print(function(513553007))

