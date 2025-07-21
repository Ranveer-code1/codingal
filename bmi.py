height=float(input("Please enter your height in centimeters"))
weight=float(input("Please enter your weight in kilograms"))
bmi= weight/(height/100)**2
print("Your BMI score is ",bmi)
if bmi<=18.4:
    print("underweight")
elif bmi<=24.9:
    print("healthy")
elif bmi<=29.9:
    print("overweight")
elif bmi<=34.9:
    print("severely overweight")
elif bmi<=39.9:
    print("obese")
else:
    print("severely obese")