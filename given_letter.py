def appears(text, letter):
    sum=0
    for char in text:
        if char==letter:
            sum+=1
    return sum 
  
def main():
    tx="aabbcca"
    x="a"
    print(appears(tx,x))

if __name__=="__main__":
    main()

