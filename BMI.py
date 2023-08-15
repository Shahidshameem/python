weight=int(input("enter the weight in kg:"))
height=float(input("enter the height in meters:"))
bmi=(weight/(height**2))
print(bmi)
if bmi<16.0:
    print("person is underweight and has severe thinness")
elif bmi<=16.9:
    print("person is underweight and has moderate thinness")
elif bmi<=18.4:
    print("the person is underweight and has mild thinness")
elif bmi<=24.9:
    print("person has normal weight")
elif bmi<=29.9:
    print("person has overweight")
else:
    print("obese")

