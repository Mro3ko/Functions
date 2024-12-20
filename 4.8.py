def time_string(hours, minutes, time_format):
    if time_format == '24':
        if hours < 10:
            hours_str = '0' + str(hours)
        else:
            hours_str = str(hours)
        
        if minutes < 10:
            minutes_str = '0' + str(minutes)
        else:
            minutes_str = str(minutes)
        
        return hours_str + ':' + minutes_str
    
    else:
        if hours < 12:
            period = 'am'
        else:
            period = 'pm'
        
        if hours == 0:
            hour_12 = 12
        elif hours > 12:
            hour_12 = hours - 12
        else:
            hour_12 = hours
        
        if minutes < 10:
            minutes_str = '0' + str(minutes)
        else:
            minutes_str = str(minutes)
        
        return str(hour_12) + ':' + minutes_str + period


print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))
