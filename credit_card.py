def hide(card_number):
    new_number=card_number[0:2]+"************"+card_number[14:16]
    return new_number

def main():
    num="5290312400019022"
    print(hide(num))

if __name__=="__main__":
    main()