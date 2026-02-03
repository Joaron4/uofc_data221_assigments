# Question 3 (1 Point)
"""
In this task, you will identify lines that are nearly identical after basic normalization.
wo lines are considered near-duplicates if they become identical after converting to lower-
case and removing all whitespace and punctuation characters.
Using sample-file.txt:
• Identify sets of near-duplicate lines.
• Print the number of such sets.
• Print the first two sets you find, including line numbers and original line
"""

def eliminate_punctuation(word):
    punctuation = '''.!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for p in punctuation:
        word = word.replace(p, "")
    return word


fhand = open('data/input/sample-file.txt', 'r')
lines = fhand.read().split('\n')
fhand.close()
normalized_lines = [eliminate_punctuation(line).strip().lower() for line in lines]




