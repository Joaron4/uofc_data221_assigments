# Question 1 (1 Point): Controlled Multiplication Loop
#------------------------------------------------------------------------
"""Write a Python program that multiplies consecutive integers starting from 1 until the product first
becomes greater than a given threshold value.
Your program should:
• Store the threshold value in a variable.
• Keep track of the current multiplier.
• Print the final product and the integer that caused the product to exceed the threshold."""

threshold = 1000  
product = 1
current_number = 1

print("current multiplier:", current_number)

while product <= threshold:
    product *= current_number
    if product > threshold:
        break
    current_number += 1
    print("current multiplier:", current_number)

print(f"Final product: {product}")