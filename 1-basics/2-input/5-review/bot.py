from random import *

# introduce Beep
print("""
 ##########
## -    O ##
## \\____/ ##
 ##########
     ##    
 ##########
## ------ ##
## 0\"     ##
##        ##
##        ##
 #        #
 ##########""")
print("""Beep:  \"Hello! I'm Beep the robot.
\tCould you give me a new eye?\"""")

beepEye = input("\nPlease enter a character for the eye: ")

#Show Beep with the user inputted beepEye

print("""
 ##########
## """ + beepEye + """    O ##
## \\____/ ##
 ##########
     ##    
 ##########
## ------ ##
## 0\"     ##
##        ##
##        ##
 #        #
 ##########""")

 #Prompt questions for BMI calculation.
 
name = str(input("Beep:  \"Thank you! What is your name, human?\" "))

age = int(input("Beep:  \"How old are you (in years)?\" "))

height = float(input("Beep:  \"How tall are you (in meters)?\" "))

weight = float(input("Beep:  \"How much do you weigh (in kilograms)?\" "))

bmi = round((weight / (height * height)), 2)

print("Beep:  \"" + str(name) + ", you are " + str(age) + " years old and your BMI is " + str(bmi) + ".\"")
 
print("\nBeep:  \"Calculating Health, Energy and Shields!")

lives = randrange(1, 10)
energy = randrange(1,10)
shield = randrange(1,10)

count = 0
print("Lives:  ", end = ''),
while count < lives:
    print("♥", end = '')
    count += 1

count = 0
print("\nEnergy: ", end = ''),
while count < energy:
    print("♦", end = '')
    count += 1

count = 0
print("\nShield: ", end = ''),
while count < shield:
    print("♦", end = '')
    count += 1

print("\n")