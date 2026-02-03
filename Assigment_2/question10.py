# Question 10 (1 Point)
"""
This final question asks you to design a reusable function for searching within text files.
Write a function:
1 def find_lines_containing(filename, keyword):
2 
3 Returns a list of (line_number, line_text) for lines that contain ←↩
keyword
4 (case-insensitive). Line numbers start at 1.
5 
Test the function using sample-file.txt with keyword lorem.

• Print how many matching lines were found.
• Print the first 3 matching lines (line number and text)

"""

def find_lines_containing(filename, keyword):
    matching_lines = []
    keyword_lower = keyword.lower()
    with open(filename, 'r') as fhand:
        count = 1
        for  line_text in fhand:
            if keyword_lower in line_text.lower():
                matching_lines.append((count, line_text.strip()))
            count += 1
    fhand.close()
    return matching_lines
MATCHING_LINES = find_lines_containing('data/input/sample-file.txt', 'Data Science')

print(f"matching lines: {len(MATCHING_LINES)}")
print("First 3 matching lines:")
for line in MATCHING_LINES[:3]:
    print(f"{line[0]}: {line[1]}")