#Question 4 (1 Point)
"""
This question involves filtering tabular data and saving the results to a new file.
Using student.csv:
• Load the dataset into a DataFrame.
• Filter students where studytime ≥ 3, internet = 1, and absences ≤ 5.
• Save the filtered data to high_engagement.csv.
• Print the number of students saved and their average grade.
"""
import pandas as pd 

student_data = pd.read_csv('data/input/student.csv')
filtered_students = student_data[(student_data['studytime'] >= 3) & 
                                 (student_data['internet'] == 1) & 
                                 (student_data['absences'] <= 5)]
filtered_students.to_csv('data/output/high_engagement.csv', index=False)
print(f"Number of students saved: {len(filtered_students)}")
average_grade = filtered_students.grade.mean()
print(f"Average grade: {average_grade}")