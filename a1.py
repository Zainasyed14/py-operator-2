w = float(input("Enter your weight in kg : "))
h = float(input("Enter your height in metres : "))

bmi = round(w/h**2 , 2)
print("your bmi is " , bmi)

if bmi<18:
    print("you are underweight")
elif bmi>=18 and bmi<24:
    print("you are normal weight ")
else:
    print("you are obese")