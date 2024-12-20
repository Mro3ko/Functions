def pts_to_grade(test_result):
    if test_result < 10:
        return "Fail"
    elif test_result >= 18:
        return "Excellent"
    elif test_result >= 14:
        return "Good"
    elif test_result >= 10:
        return "Satisfactory"
    
test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')