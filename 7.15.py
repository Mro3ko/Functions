def function(text):
    count=0
    for i in text:
        if i=="+":
            count+=1
        elif i=="-":
            count-=1
        
        if count==3:
            return True
    return False

print(function("+-+++-+---"))
print(function("+-+-+-+-"))
print(function("+-++-+--"))
print(function("+-++-++-+---"))