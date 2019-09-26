name = str(input("What is your name, human?\n"))

age = int(input("\nHow old are you (in years)?\n"))

height = float(input("\nHow tall are you (in meters)?\n"))

weight = float(input("\nHow much do you weigh (in kilograms)?\n"))

bmi = round((weight / (height * height)), 2)

print("\n" + str(name) + " you are " + str(age) + " years old and your BMI is " + str(bmi))