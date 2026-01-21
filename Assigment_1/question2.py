# Question 2 (1 Point): Nested Dictionary from Strings
#------------------------------------------------------------------------
"""
Define a function that receives a list of strings and returns a dictionary with the following struc-
ture:
• Each key is a string from the list.
• Each value is another dictionary containing:
– The length of the string
– Whether the length is even or odd 

"""
def string_list_to_nested_dict(string_list):
    result = {}
    for i in string_list:
        word_length = len(i)
        if word_length % 2 == 0:
            parity = 'even'
        else:
            parity = 'odd'
        result[i] = {
            'length': word_length,
            'parity': parity
        }
    return result
print(string_list_to_nested_dict(['data','science']))