def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result= 'Wednesday'
    elif day_number == 4:
        result= 'Thursday'
    elif day_number == 5:
        result= 'Friday'
    elif day_number == 6:
        result= 'Saturday'
    elif day_number == 7:
        result= 'Sunday'
    return result

for i in range(1,8):
    print(day_name(i))