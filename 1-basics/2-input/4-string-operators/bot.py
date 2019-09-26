lives = int(input("Please enter the number of lives: "))
energy = int(input("Please enter the energy level: "))
shield = int(input("Please enter the shield level: "))

print("\nHealth has been set.\n")

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