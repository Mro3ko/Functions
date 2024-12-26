def f(dice):
    streak=1
    max_streak=1
    result=dice[0]
    for i in range(1,len(dice)):
        if dice[i]==dice[i-1]:
            streak+=1
            if streak>max_streak:
                max_streak=streak
                result=dice[i]
        else:
            streak=1
    return result

print(f("5233165554211"))
print(f("2133"))


    