# Question 4 (10 points)
"""
Using the training and testing data from Question 3, train a K-Nearest Neighbors classifier. Set
the number of neighbors to k = 5. Train the model using the training data. Then use the trained
model to predict the labels of the test data.
After making predictions:
• Compute and display the confusion matrix
• Compute and print Accuracy
• Compute and print Precision
• Compute and print Recall
• Compute and print F1-score
Then write comments in your code (5–7 sentences) explaining:
• What True Positive, True Negative, False Positive, and False Negative mean in the context
of kidney disease prediction
• Why accuracy alone may not be enough to evaluate a classification model
• Which metric is most important if missing a kidney disease case is very serious, and why

"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import numpy as np

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

# Train KNN model
knn_model = KNeighborsClassifier(n_neighbors=5)
trained_knn_model = knn_model.fit(features_train, labels_train)



# Make predictions
predictions = trained_knn_model.predict(features_test)



# Evaluate the model
print("\n=== Model Evaluation ===")
print(f"Accuracy: {accuracy_score(labels_test, predictions):.4f}")
print(f"Precision: {precision_score(labels_test, predictions):.4f}")
print(f"Recall: {recall_score(labels_test, predictions):.4f}")
print(f"F1 Score: {f1_score(labels_test, predictions):.4f}")
print("\nConfusion Matrix:")
print(confusion_matrix(labels_test, predictions))   

#Response 
"""
1. What True Positive, True Negative, False Positive, and False Negative mean in the context
of kidney disease prediction
- True Positive (TP): The model correctly predicts that a patient has kidney disease (CKD).
- True Negative (TN): The model correctly predicts that a patient does not have kidney disease (non-CKD).
- False Positive (FP): The model incorrectly predicts that a patient has kidney disease when they do not.
- False Negative (FN): The model incorrectly predicts that a patient does not have kidney disease when they actually do .

2. Why accuracy alone may not be enough to evaluate a classification model
- Accuracy can be misleading,for example, if in my model 90% of the patients do not have kidney disease, 
my model can always predicts "no CKD" and  would achieve 90% accuracy, but it 
would fail to identify any actual cases of kidney disease.

3. Which metric is most important if missing a kidney disease case is very serious, and why
- In this case, Recall is the most important metric because it measures teh true responses , meaning the ones correctly identified with
kidney disease  .

"""

