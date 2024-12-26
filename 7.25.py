def function(x,y):
    result=0
    for i in range(x,y+1):
        if i%2==0 and i%3==0 and not i%4==0:
            result+=i
    return result
print(function(1,20))
print(function(10,30))