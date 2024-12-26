import range
x=int(input("podaj dolną granicę przedziału: "))
y=int(input("podaj górną granicę przedziału: "))
a=int(input("jakiej liczby szukamy: "))

print(f"liczba {a} w przedziale <{x},{y}>: {range.within(x,y,a)}")