# Question 1 (1 Point)
"""
In this question, you will practice reading a text file and performing 
basic text preprocessing
before computing word statistics.
Using sample-file.txt:
• Read the file and split it into tokens (words).
• Convert all tokens to lowercase.
• Remove punctuation characters from the beginning and end of each token.
• Keep only tokens that contain at least two alphabetic characters.
• Count word frequencies and print the 10 most frequent words in descending order in the
format: word -> count.
"""

def eliminate_punctuation(word):
    punctuation = '''.!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for p in punctuation:
        word = word.replace(p, "")
    return word

#______________________
def contains_alphabetic(word):
    alpha_count = 0
    for i in range(len(word)):
        if word[i].isalpha():
            alpha_count += 1

    if alpha_count < 2:
        return False
    else:
        return True
#__________________________

fhand = open('data/input/sample-file.txt', 'r')
raw_text = fhand.read()
tokens = raw_text.split()
tokens_lower = [eliminate_punctuation(word).strip().lower() for word in tokens]
alphabetic_tokens = [word for word in tokens_lower if contains_alphabetic(word)]
word_frequency_dictionary = {}
#- dictionary to count word frequency
for word in alphabetic_tokens:
    if word in word_frequency_dictionary:
        word_frequency_dictionary[word] += 1
    else:
        word_frequency_dictionary[word] = 1

# -------top 10

for _ in range(min(10, len(word_frequency_dictionary))):
    max_count = -1
    max_word = None
    for word, count in word_frequency_dictionary.items():
        if count > max_count:
            max_count = count
            max_word = word
    print(f"{max_word} -> {max_count}")
    del word_frequency_dictionary[max_word] 