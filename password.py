def password_len(password):
    return len(password)>5

def password_uniqe(password):
    for char in password:
        if password.count(char)>1:
            return False
    
    return True

def password_valid(password):
    if password_len(password) and password_uniqe(password):
        return True
    else:
        return False
    
def main():
    password="abcdqwer"
    print(password_valid(password))

if __name__=="__main__":
    main()

