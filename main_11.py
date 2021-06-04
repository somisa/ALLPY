# Task 1 - print numbers in a shape of a triangle
for i in range(1,11):
    for j in range(i):
        print(i,end=' ')
    print("")

# Task 2 - numbers from 1300 to 2100 that are divisible by 7 and multiple of 4
for i in range(1300,2101):
    if i % 7 == 0 and i % 4 == 0:
        print(i,end=' ')
print("")

# Task 3 - print all the possible names
first_name = ["Amy", "Jake", "Raymond", "Charles"]
last_name = ["Peralta", "Santiago", "Holt", "Boyle"]
for i in first_name:
    for j in last_name:
        print(i, j) # the same as print(i + " " + j)

# Task 4 - find all the pairs in the list
names = ["Martin", "Steven", "Quentin", "Alfred", "Tim", "Christopher", "James"]
for i in range(len(names)):
    for j in range(len(names)):
        if i < j:
            print(names[i] + " and " + names[j])

# Task 5 - python turtle commands
'''
go() - the turtle goes forward
turn() - the turtle turns in degrees
width() - the width of the pen
color("") - the color of the pen
reset() - clears the screen and puts the turtle back
clear() - clears the screen from all the drawings
invisible() - hides the turtle
visible() - shows the turtle
pen_up() - puts down the pen
pen_down() - picks up the pen
'''
# These programs can only be used in the PythonTurtle software
# Task 6 - draw a triangle
for i in range(3):
    go(50)
    turn(120)

# Task 7 - draw shapes from triangle to octagon
reset()
angles = 3
for i in range(6):
    width(angles)
    for j in range(angles):
        go(50)
        turn(360/angles)
    angles += 1

# Task 8 - draw a house
"""
- draw a square/rectangle house with for loop
- go to a new position and draw a door with a for loop
- go to the top and draw a roof with a new color
- draw two windows next to each other with nested for loops
- draw a fence next to the house with a for loop
"""

# Task 9 - is it a prime number
my_number = int(input("Give me a number: "))
prime_divisors = []
for i in range(1,my_number+1):
    if my_number % i == 0:
        prime_divisors.append(i)
if len(prime_divisors) > 2:
    print(str(my_number) + " is not a prime number because it has " + str(len(prime_divisors)) + " divisors. These divisors are:" + str(prime_divisors))
else:
    print(str(my_number) + " is a prime number because it has only " + str(len(prime_divisors)) + " divisors, one and itself.")

# Task 10 - rotating a list
list = [1,2,3,4,5,6]
print(list)
rotate = int(input("How much you want to rotate on the list?\n"))
rotate = rotate % 6
direction = input("In which direction do you want to rotate?(left/right)\n")
if direction == "left":
    list = list[rotate:] + list[:rotate]
else:
    list = list[-rotate:] + list[:-rotate]
print(list)
