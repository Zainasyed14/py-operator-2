a = float(input("Enter your number"))
b = float(input("Enter your second number"))
c = float(input("Enter your third number"))

if a>b and a>c:
    print(a , "is larger")
elif b>a and b>c:
    print(b , "is larger")
else:
    print(c , "is larger")