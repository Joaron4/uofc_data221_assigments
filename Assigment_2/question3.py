def eliminate_punctuation(word):
    punctuation = '''.!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for p in punctuation:
        word = word.replace(p, "")
    return word

fhand = open('data/input/sample-file.txt', 'r')
lines = fhand.read().split('\n')
fhand.close()

normalized_lines = [eliminate_punctuation(line).replace(" ", "").strip().lower() for line in lines]

groups = {}
for i in range(len(lines)):
    norm = normalized_lines[i]
    if norm != "":
        if norm not in groups:
            groups[norm] = []
        groups[norm].append((i + 1, lines[i]))

duplicate_sets = []
for key in groups:
    if len(groups[key]) > 1:
        duplicate_sets.append(groups[key])


for set_num in range(min(2, len(duplicate_sets))):
    print(f"Set {set_num + 1}:")
    for line_num, original_line in duplicate_sets[set_num]:
        print(f"{line_num}: {original_line}")