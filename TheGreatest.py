# Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:



# Input
# The input file contains 3 integer values.

# Output
# Print the greatest of these three values followed by a space and the message “eh o maior”.

numbers = (input().split(' '))
numbers2 = []

for i in range (len(numbers)):
    t = int(numbers[i])
    numbers2.append(t)

print("{} eh o maior".format(max(numbers2)))

