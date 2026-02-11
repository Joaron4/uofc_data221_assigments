# Question 5 (5 points)
"""
Using the same training and testing data, train multiple KNN models using different values of k.
Train models for:
k = 1, 3, 5, 7, 9
For each value of k, compute the test accuracy and store the results. Create a small table
showing each value of k and its corresponding accuracy.
Identify which value of k gives the highest test accuracy.
Finally, write comments in your code (3–5 sentences) explaining:
 How changing k affects the behavior of the model
• Why very small values of k may cause overfitting
• Why very large values of k may cause underfitting
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load and prepare data
kidney_data = pd.read_csv('./data/input/kidney_disease.csv')
kidney_data.classification = kidney_data.classification.str.replace('ckd\t', 'ckd')
kidney_data['label_y'] = kidney_data.classification.apply(lambda x: 1 if x == 'ckd' else 0)

# Create an explicit copy to avoid warnings
feature_matrix = kidney_data[kidney_data.columns.difference(['label_y','classification'])].copy()
target_vector = kidney_data['label_y']

# Handle missing values 

categorical_cols = {"appet", "ane", "ba", "cad", "dm", "htn", "pc", "pcc", "pe", "rbc"}  

for col_name in feature_matrix.columns:
    # Clean the column
    feature_matrix[col_name] = feature_matrix[col_name].astype(str).str.strip()
    feature_matrix[col_name] = feature_matrix[col_name].replace(["N/A", "?", "\t?", "nan", "None", ""], np.nan)
    
    if col_name in categorical_cols:
        # For categorical columns
        mode_val = feature_matrix[col_name].mode()
        if len(mode_val) > 0:
            feature_matrix[col_name] = feature_matrix[col_name].fillna(mode_val[0])
        else:
            # default for categorical
            feature_matrix[col_name] = feature_matrix[col_name].fillna('unknown')
        feature_matrix[col_name] = feature_matrix[col_name].astype('category').cat.codes
    else:
        # For numerical columns
        feature_matrix[col_name] = pd.to_numeric(feature_matrix[col_name], errors='coerce')
        median_val = feature_matrix[col_name].median()
        #if nan values
        if pd.isna(median_val):
            median_val = 0
        
        feature_matrix[col_name] = feature_matrix[col_name].fillna(median_val)
        feature_matrix[col_name] = feature_matrix[col_name].astype(float)


# Train/test split
features_train, features_test, labels_train, labels_test = train_test_split(
    feature_matrix, target_vector, test_size=0.2, random_state=42
)
accuracy_scores = {}
for i in range(1, 10, 2):
    knn_model = KNeighborsClassifier(n_neighbors=i)
    trained_knn_model = knn_model.fit(features_train, labels_train)
    predictions = trained_knn_model.predict(features_test)
    accuracy = accuracy_score(labels_test, predictions)
    accuracy_scores[i] = accuracy

accuracy_table = pd.DataFrame(list(accuracy_scores.items()), columns=['k', 'Accuracy'])
print(accuracy_table)
plt.figure()
plt.plot(accuracy_table['k'], accuracy_table['Accuracy'], marker='o')
plt.title('KNN Accuracy for Different Values of k')
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.savefig('graphs/question05_knn_accuracy.png')

# Response
"""
1. A smaller k means that the model will be more sensitive to noise in the training data, which can lead to overfitting. 
so for example with k = 1 the model will not be good at generalizing to unseen data, as it will simply memorize the training data.
2. A larger k means that the model will be more general and less sensitive to noise, which can lead to underfitting. for example with k = 9 
the model may be too simple to capture the underlying patterns in the data, and may not perform well on the test set.

As oresented in the graph, the accuracy is highest for k = 3, which suggests that this value of k provides a good balance between bias and variance for this dataset.|
"""




