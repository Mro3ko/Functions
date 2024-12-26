def within(x,y,a):
    if x<=a<=y:
        return "yes"
    else:
        return "no"

def main():
    x=1
    y=10
    z=11
    print(within(x,y,z))

if __name__=="__main__":
    main()
