import math
def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    for i in range(3,math.floor(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True



def nth_prime(n):
    prime_found=0
    number=2
    while prime_found<n:
        if is_prime(number):
            prime_found+=1
        number+=1
    return number-1
for i in range (1,11):
    print(nth_prime(i))