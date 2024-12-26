def valid_binary(a):
    for char in a:
        valid=True
        if char =="0" or char=="1":
            continue
        else:
            valid=False
            break
    return valid

binary=input("Enter a number: ")
print(f"{binary} is valid binary number: {valid_binary(binary)}")
