# Question 3 (1 Point): Safe Function Application
#------------------------------------------------------------------------
"""
Define a function that computes x**y. Then, given a list of pairs (x, y):
• Use a for loop with argument unpacking to call the function.
• Skip any pair where the exponent y is negative.
• Store the valid results in a list and print the list.x|x
"""
def power_calculator(base, exponent):
    return base ** exponent

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
results = []
for base, exponent in pairs:
    if exponent < 0:
        continue
    result = power_calculator(base, exponent)
    results.append(result)
print(results)