# CTI-110
# P2HW2 - List and Sets
# Jasmine Grimes 
# 10-03-2021
#

import math

the_list = []

#input list of numbers
a = the_list.append(int(input("Enter num 1: ")))
b = the_list.append(int(input("Enter num 2: ")))
c = the_list.append(int(input("Enter num 3: ")))
d = the_list.append(int(input("Enter num 4: ")))
e = the_list.append(int(input("Enter num 5: ")))
f = the_list.append(int(input("Enter num 6: ")))

average = sum(the_list) / len(the_list)
total = sum(the_list)
length = len(the_list)
avg_list = total / length
my_set = set(the_list)


print()

#show created list
print('Created list\n', the_list)
      
#show smallest number in list
print("Smallest number in list:", min(the_list))
      
#show largest number in list
print("Largest number in list:", max(the_list))

#show sum of numbers in list
print("Sum of numbers in List:", sum(the_list))

#show average of numbers in list
print("Average of numbers in List:", avg_list)

print()

#Set of numbers in list
print("Created set")
print(my_set)

