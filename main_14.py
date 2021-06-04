input_date = input("Give me today's date with this format: e.g. 2021-02-24:\n")
date = input("Give me your birth date with the same format:\n")
days = 0
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Spliting the text to list element
for i in date:
    born = date.split('-')
for j in input_date:
    date_now = input_date.split('-')
# Converting the list element from string to int
for i in range(len(born)):
    born[i] = int(born[i])
for i in range(len(date_now)):
    date_now[i] = int(date_now[i])

while (not (born[1] == date_now[1] and born[0] == date_now[0] and born[2] == date_now[2])):
    if born[1] == 2 and ((born[0] % 4 == 0 and born[0] % 100 != 0) or born[0] % 400 == 0):
        if born[2] < daysOfMonths[born[1] - 1] + 1:
            born[2] += 1
        else:
            born[1] += 1
            born[2] = 1
    else:
        if born[2] < daysOfMonths[born[1] - 1]:
            born[2] += 1
        else:
            if born[1] == 12:
                born[0] += 1
                born[1] = 1
                born[2] = 1
            else:
                born[1] += 1
                born[2] = 1
    days += 1
print("You are %s days old." % days)

# Task 2 - finding anagrams
word_1 = "Amy"
word_2 = "May"
if len(word_1) == len(word_2):
    if sorted(word_1.lower()) == sorted(word_2.lower()):
        print("These are anagrams.")
    else:
        print("These are not anagrams.")
else:
    print("These are not anagrams.")

# Task 3 - slow down
speed = [96, 98, 72, 64, 93, 61, 95, 78, 54, 51, 52, 55, 47, 70, 68, 67, 79, 83, 59, 76, 45, 82, 87, 66, 89, 62, 69, 74, 75, 48, 88, 81, 86, 97, 94, 71, 46, 57, 50, 53]
slows = 0
for i in range(len(speed)-1):
    minSpeed = speed[i+1]
    for j in range(i+1, len(speed)-1):
        if speed[j] < minSpeed:
            minSpeed = speed[j]
    if speed[i] > minSpeed:
        slows += 1
print(slows, "cars needs to slow down to avoid accidents.")

# Task 4 - voting for new burger
burgers = ["Spicy Pinata", "Cheesy Dream", "Vegan Fluffy", "Fatty Boom", "Tortuga", "Pork Pie"]
votes = [95061, 93439, 98563, 90478, 90915, 97334]

# number of new burgers
print("We have " + str(len(burgers)) + " different burgers to choose from.")

# votes per burgers
print("The votes on the different burgers are the followings:")
for i in range(len(burgers)-1):
    print(f"\t{burgers[i]}: {votes[i]} votes")  # using f"string"
    
# winner of the competition
index = 0
for i in range(len(votes)-1):
    if votes[index] < votes[i]:
        index = i
print("The winner is %s ." % burgers[index])

# number of votes
number_of_votes = 0
for i in votes:
    number_of_votes += i
print(number_of_votes, " people voted in the game.")
