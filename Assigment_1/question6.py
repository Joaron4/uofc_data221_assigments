# Question 6 (1 Point): Distribution Analysis
#------------------------------------------------------------------------
"""
Define a function that receives a list of numbers and returns a dictionary where:
• Each key is a unique value from the list.
• Each value is the percentage of elements in the list that are less than or equal to that key.
The resulting dictionary should be sorted by key before being returned.
"""
def distribution_analysis_of_list(list_of_numbers):
    distribution_dictionary = {}
    set_of_numbers = set(list_of_numbers)
    sorted_unique_numbers = sorted(set_of_numbers)
    len_of_list_of_numbers = len(list_of_numbers)
    for key in  sorted_unique_numbers:
        count_of_elements_less_or_equal = 0
        for value in list_of_numbers:
            if value <= key:
                count_of_elements_less_or_equal += 1
        distribution_dictionary[key] = (count_of_elements_less_or_equal / len_of_list_of_numbers) * 100
    return distribution_dictionary 



numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis_of_list(numbers))