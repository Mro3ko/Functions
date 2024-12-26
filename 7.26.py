def function(text):
    text_dash=""
    for i in range(len(text)):
        text_dash+=text[i]
        if i<len(text)-1:
            text_dash+="-"
    return text_dash

print(function("Univesity"))
print(function("UE"))
print(function("x"))
print(function(""))