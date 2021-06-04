# Task 1 - data from list
length_of_list = 10
numbers = []
while length_of_list > 0:
    new_number = int(input("Enter a number\n"))
    numbers.append(new_number)
    length_of_list -= 1
odd = 0
even = 0
positive = 0
negative = 0
zero = 0
for i in numbers:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Evens: " + str(even) + "\nOdds: " + str(odd) + "\nPositives: " + str(positive) + "\nNegatives: " + str(negative) + "\nZeros: " + str(zero))


# Task 2 - removing duplications from list
nums = [1, 2, 3, 4, 5, 6, 5, 4, 5, 6, 1, 0, 1, 3]
print(str(nums))
new_nums = []
skipped_nums = 0
for i in nums:
    if i not in new_nums:
        new_nums.append(i)
    else:
        skipped_nums += 1
nums = new_nums
print(str(nums))
print("Skipped numbers: " + str(skipped_nums))

# Task 3 - extend command
list = [1, 2, 3, 4]
print(list)
#list.extend(5) #comment this line to remove the error from the code
print(list)
list.extend("Hello there")
print(list)
list.extend([5, 6, "General Kenobi"])
print(list)
list.append([7, 8, 9])
print(list)

# Task 4 - find integers in list
everything_list = [2, 3, 3.14, "Bob", -2, 3, 42, True, "null", False, 0]
integers_list = []
for i in everything_list:
    if type(i) == int:
        integers_list.append(i)
print(integers_list)

# Task 5 - largest gap in a list
random_numbers = [12, 33, 39, 83, 75, 28, 79, 52, 34, 57, 95, 40, 73, 13, 24, 26, 93, 68, 48, 45, 10, 87, 37, 20, 85, 99, 98, 92, 81, 43,  9, 31, 91, 67, 46, 66, 25, 76,  7, 61, 15, 63, 41, 71, 19, 22, 62, 35, 90, 97, 30, 78, 60,  2, 50,  1, 42, 94, 51, 96, 69, 77, 58, 47, 53, 54, 70,  3, 84, 14, 86, 56, 89,  8,  5, 38, 44, 18, 88, 23, 65, 74, 16, 82, 64, 100, 27, 59, 29, 72, 17, 55, 49, 21, 80, 11, 36, 6, 4, 32]
smallest = min(random_numbers)
greatest = max(random_numbers)
print("The smallest number is " + str(smallest) + ".")
print("The greatest number is " + str(greatest) + ".")
print("The smallest number is at index " + str(random_numbers.index(smallest)) + ".")
print("The greatest number is at index " + str(random_numbers.index(greatest)) + ".")
biggest_gap = greatest - smallest
print("The gap between these numbers is " + str(biggest_gap) + ".")

# Task 6 - largest and second largest numbers
my_list = [2, 7, 3, 1, 8, 4]
print(my_list)
index = 0
largest_number = my_list[0]
while index < len(my_list):
    if largest_number < my_list[index]:
        largest_number = my_list[index]
        largest_index = index
    index += 1
print(largest_index)
second_largest_number = my_list[0]
index = 0
while index < len(my_list):
    if largest_number != my_list[index] and second_largest_number < my_list[index]:
        second_largest_number = my_list[index]
    index += 1
diff = largest_number - second_largest_number
largest_number -= diff
my_list[largest_index] = largest_number
my_list.insert(largest_index+1, diff)
print(my_list)
print("The largest number was " + str(largest_number+diff) + ". The second largest was " + str(second_largest_number) + ".")

# Task 7 - sorting a list
list_to_sort = [41, 4, 13, 43, 30, 22, 11,  5, 38, 92, 36, 33, 35, 26, 85, 95, 68, 56, 62, 55, 75, 73, 42, 88, 54, 64, 78]
print(list_to_sort)
sorted = False
while not sorted:
    i = 0
    sorted = True
    while i < len(list_to_sort)-1:
        if list_to_sort[i] > list_to_sort[i+1]:
            temp = list_to_sort[i]
            list_to_sort[i] = list_to_sort[i+1]
            list_to_sort[i+1] = temp
            sorted = False
        i += 1
print(list_to_sort)
