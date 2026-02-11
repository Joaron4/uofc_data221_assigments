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

kidney_data = pd.read_csv('data/input/kidney_disease.csv')
kidney_data.classification = kidney_data.classification.str.replace('ckd\t', 'ckd')
kidney_data['label_y'] = kidney_data.classification.apply(lambda x: 1 if x == 'ckd' else 0)
feature_matrix = kidney_data[kidney_data.columns.difference(['label_y','classification'])]
target_vector = kidney_data['label_y']
features_train, features_test, labels_train, labels_test = train_test_split(
    feature_matrix, target_vector, test_size=0.3, random_state=42
)

# Response
"""
1. We should split the data into a training set and a testing set, to compare how good is our model and generalizing. If
we didn't divide it our model would be trained and tested on the same data, which would lead to overfitting. 
2. It's to evaluate the performance of our model on unseen data, and check how well it generalizes unseen information.
"""
