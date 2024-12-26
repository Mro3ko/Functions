def function(amount):
    result=0

    result+=amount//5
    amount%=5

    result+=amount//2
    amount%=2

    result+=amount
    return result

print(function(123))
