#Task 1 - find all the common values in the two lists
list_1 = [61, 5, 6, 28, 87, 52, 89, 51, 86, 29, 93, 26, 99, 16, 36, 53, 47, 95, 18, 54, 62, 37, 34, 11, 75, 90, 88, 24, 72, 76, 55, 44,  3, 50, 35, 17, 94,  7, 31,100, 42, 43, 74, 83, 82,  4, 10]
list_2 = [5, 9, 62, 79, 17, 68, 54, 50, 60, 89, 29, 41, 83, 77,  3, 86, 56, 13, 26, 52, 98, 81, 82, 74, 55, 66, 92, 61, 30, 37, 57, 91,  2, 71, 93, 35, 33, 24,100, 19, 65, 95, 90, 38, 88, 31, 80, 70, 25, 39, 15, 85, 42, 94, 11, 76, 32,  7, 48]
common_values = []
for i in list_1:
    for j in list_2:
        if i == j:
            common_values.append(i)
print(common_values)

#Task 2 - create one number from the list values
numbers = [12, 54, 812]
whole_number = ""
for i in numbers:
    whole_number += str(i)
whole_number = int(whole_number)
print(whole_number)
print(type(whole_number))

# Task 3 - make two lists the same
list_1 = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20,  36, 48]
list_2 = [ 36, 44, 20, 96, 69, 15, 27, 14, 87, 67, 97, 43,  8, 22]
print(list_1)
print(list_2)
for i in list_1:
    if i not in list_2:
        list_2.append(i)
for i in list_2:
    if i not in list_1:
        list_1.append(i)
list_1.sort()
list_2.sort()
print(list_1)
print(list_2)

# Task 4 - is the list sorted / is the list strictly increasing
list = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20,  36, 48]
print(list)
sorted = True
index = 0
while sorted and index < len(list)-1:
    if list[index] > list[index+1]:
        sorted = False
    else:
        index += 1
if sorted:
    print("The list is sorted.")
else:
    print("The list is not sorted.")

# Task 5 - price of items in a shop
items = ["apple", "book", "bread", "cheese", "chicken", "curry sauce", "doughnut", "toilet roll", "socks", "toothpaste"]
prices = [1500, 1000, 700, 1600, 1900, 600, 800, 999, 500, 550]
to_buy = []
for i in range(len(prices)):
    if prices[i] < 1000:
        to_buy.append(items[i])
print(to_buy)

# Task 6 - 100. Fibonacci number
a_1 = 1
a_2 = 1
series = [a_1, a_2]
for i in range(98):
    series.append(series[-2]+series[-1])
print(series[-1])

# Task 7 - 400m running results
names = ["Bob", "Wanda", "Jared", "Emma", "Lisa", "Fred", "George", "Noah", "Rachel"]
times = [123.42, 67.15, 80.70, 118.40, 99.95, 68.22, 71.51, 102.68, 80.88]
for i in range(len(times)):
    for j in range(len(times)-1):
        if times[j] > times[j+1]:
            times[j], times[j+1] = times[j+1], times[j]
            names[j], names[j + 1] = names[j + 1], names[j]
print(names)
print(times)

# Task 8 - price of the translation
string = """Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly
normal, thank you very much. They were the last people you’d expect to be involved in anything
strange or mysterious, because they just didn’t hold with such nonsense.
 Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy
man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin
and blonde and had nearly twice the usual amount of neck, which came in very useful as she
spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys
had a small son called Dudley and in their opinion there was no finer boy anywhere.
 The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was
that somebody would discover it. They didn’t think they could bear it if anyone found out about
the Potters. Mrs. Potter was Mrs. Dursley’s sister, but they hadn’t met for several years; in fact,
Mrs. Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing
husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the
neighbors would say if the Potters arrived in the street. The Dursleys knew that the Potters had a
small son, too, but they had never even seen him. This boy was another good reason for keeping
the Potters away; they didn’t want Dudley mixing with a child like that.
 When Mr. and Mrs. Dursley woke up on the dull, gray Tuesday our story starts, there was
nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be
happening all over the country. Mr. Dursley hummed as he picked out his most boring tie for
work, and Mrs. Dursley gossiped away happily as she wrestled a screaming Dudley into his high
chair.
 None of them noticed a large, tawny owl flutter past the window.
 At half past eight, Mr. Dursley picked up his briefcase, pecked Mrs. Dursley on the cheek, and
tried to kiss Dudley good-bye but missed, because Dudley was now having a tantrum and
throwing his cereal at the walls. """
price_1 = 2 * len(string)
print(price_1)
words = 1
for i in string:
    if i == " ":
        words += 1
price_2 = 12 * words
print(price_2)

# Task 9 - getting information from a person
name = ["Bob", "Wanda", "Jared", "Emma", "Lisa", "Fred", "George", "Noah", "Rachel"]
age = [26, 31, 35, 41, 58, 30, 46, 61, 25]
gender = ["male", "female", "male", "female", "female", "male", "male", "male", "female"]
job = ["web developer", "marketing director", "content creator", "human resources", "CEO", "software developer", "public relations manager", "tester", "sales representative"]
salary = [1500, 1500, 1400, 1300, 1400, 1500, 1400, 1300, 1500]
i = 0
for i in range(len(name)-1):
    for j in range(i+1, len(name)):
        if name[i] > name[j]:
            name[i], name[j] = name[j], name[i]
            age[i], age[j] = age[j], age[i]
            gender[i], gender[j] = gender[j], gender[i]
            job[i], job[j] = job[j], job[i]
            salary[i], salary[j] = salary[j], salary[i]
print(name)
print(age)
print(gender)
print(job)
print(salary)
