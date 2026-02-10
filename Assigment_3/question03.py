# Question 3 (5 points)
"""
Load kidney disease.csv into a pandas DataFrame. Create a feature matrix X that contains all
columns except CKD. Create a label vector y using the CKD column.
Then split the dataset into:
• Training data (70%)
• Testing data (30%)
Use train test split with a fixed random state.
After performing the split, write comments in your code explaining:
• Why we should not train and test a model on the same data
• What the purpose of the testing set is
"""
import pandas as pd
from sklearn.model_selection import train_test_split
kidney_data = pd.read_csv('data/input/kidney disease.csv')
X = kidney_data.drop(columns=['CKD'])
y = kidney_data['CKD']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
