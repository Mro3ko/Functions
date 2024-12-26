def sum_of_natural(n):
    if n==1:
        return 1
    
    if n>1:
        return n+sum_of_natural(n-1)
    
print(sum_of_natural(15))