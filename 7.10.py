def function(x,y):
    if x>y:
        x,y = y, x
    sum=0
    for i in range(x,y+1):
        if i<0 and i%2==0:
            sum+=1
    return sum

print(function(-7,8))
print(function(-1,11))