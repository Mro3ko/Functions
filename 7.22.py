def function(text):
    acronym=text[0]
    for i in range(1,len(text)):
        if text[i-1]==" ":
            acronym+=text[i]
    
    return acronym

print(function("Internet of Things"))
print(function("For Your Information"))
print(function("Python"))
print(function("A dog"))
