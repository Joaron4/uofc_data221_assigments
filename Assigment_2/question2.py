# Question 2 (1 Point)
"""
In this question, you will analyze pairs of consecutive words (called bigrams) from a text file.
Using sample-file.txt:
• Read the file and split it into tokens (words).
• Convert all tokens to lowercase.
• Remove punctuation characters from the beginning and end of each token.
• Keep only tokens that contain at least two alphabetic characters.
• Construct bigrams (pairs of consecutive cleaned words).
• Count the frequency of each bigram.
• Print the 5 most frequent bigrams in descending order in the format: word1 word2 ->
count
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
fhand.close()
tokens = raw_text.split()
tokens_lower = [eliminate_punctuation(word).strip().lower() for word in tokens]
alphabetic_tokens = [word for word in tokens_lower if contains_alphabetic(word)]
bigrams = []
#- construct bigrams
for i in range(len(alphabetic_tokens)-1):
    if i < len(alphabetic_tokens):
        bigram = alphabetic_tokens[i] + " " + alphabetic_tokens[i + 1]
        bigrams.append(bigram)

#_____word frequency dictionary 
bigram_frequency_dictionary = {}
for bigram in bigrams:
    if bigram in bigram_frequency_dictionary:
        bigram_frequency_dictionary[bigram] += 1
    else:
        bigram_frequency_dictionary[bigram] = 1
# -------top 5

for _ in range(min(5, len(bigram_frequency_dictionary))):
    max_count = -1
    max_bigram = None
    for bigram, count in bigram_frequency_dictionary.items():
        if count > max_count:
            max_count = count
            max_bigram = bigram
    print(f"{max_bigram} -> {max_count}")
    del bigram_frequency_dictionary[max_bigram]