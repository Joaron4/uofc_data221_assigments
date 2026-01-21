# Question 4 (1 Point): Sorted Search with Conditions
#------------------------------------------------------------------------
"""
Given a list of random values between 0 and 1 and a random value x:
• Sort the list.
• Find all indices where the list value is greater than or equal to x.
• Print the sorted list, the value of x, and the first matching index (if one exists).
"""
from random import random

values = [random() for i in range(20)]
index_list = []
x = random()
sorted_values = sorted(values)
for i in sorted_values:
    if i >= x:
        index_list.append(sorted_values.index(i))
    
print("Sorted Values:", sorted_values)
print("Value x:", x)
if len(index_list) == 0:
    print("No matching index found.")
else:
    print("First matching index:", index_list[0] )