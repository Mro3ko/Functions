def sum_of_digits(number):
    number = abs(number)
    number=str(number)
    sum=0
    for i in number:
        sum=sum+int(i)

       
    return sum
print(sum_of_digits(-12305))