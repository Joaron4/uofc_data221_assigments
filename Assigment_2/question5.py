# Question 5 (1 Point)
"""
Here you will create a new categorical variable and generate a grouped summary table.
Using student.csv:
• Create a new column grade_band:
– Low: grade ≤ 9
– Medium: grade 10–14
– High: grade ≥ 15
• Create a grouped summary table showing for each band:
– number of students
– average absences
– percentage of students with internet access
• Save the table as student_bands.csv.
"""
import pandas as pd
import numpy as np

def calculate_percentage_with_internet(number):
    return np.mean(number) * 100
#_______________________________________________________________________________
def grade_band_category_picker(grade):
    if grade <= 9:
        return 'Low'
    elif grade <= 14:
        return 'Medium'
    else:
        return 'High'
#_________________
student_data = pd.read_csv('data/input/student.csv')

student_data['grade_band'] = student_data['grade'].apply(grade_band_category_picker)

grouped_student_grade_band = student_data.groupby(['grade_band']).agg(
    number_of_students = ('grade', 'count'),
    average_absences = ('absences', 'mean'),
    percentage_with_internet = ('internet', calculate_percentage_with_internet)
).reset_index()
grouped_student_grade_band.to_csv('data/output/student_bands.csv', index=False)