# Question 6 (1 Point)
"""
In this question, you will create a simple category based on crime levels and compare unem-
ployment rates between the groups.
Using crime.csv:
• Load the dataset into a pandas DataFrame.
• Create a new column called risk based on ViolentCrimesPerPop:
– If ViolentCrimesPerPop is greater than or equal to 0.50, set risk = "High-
Crime".
– Otherwise, set risk = "LowCrime".
• Group the data by the risk column.
• For each group, calculate the average value of PctUnemployed.
• Print the average unemployment rate for both HighCrime and LowCrime groups in a
clear format.
"""
import pandas as pd
def risk_category_picker(violent_crime_rate):
    if violent_crime_rate >= 0.50:
        return 'HighCrime'
    else:
        return 'LowCrime'
#________________________________________________
crime_data = pd.read_csv('data/input/crime.csv')
crime_data['risk'] = crime_data.ViolentCrimesPerPop.apply(risk_category_picker)

average_unemployment_by_risk = crime_data.groupby('risk').PctUnemployed.mean().reset_index()
for i in average_unemployment_by_risk.iterrows():
    print(f"Average unemployment rate for {i[1].risk}: {round(i[1].PctUnemployed*100,2)}%")