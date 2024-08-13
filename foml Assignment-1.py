# -*- coding: utf-8 -*-
"""FOMLa1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19nQXx6Q9deLRTMsAdMhDWBzVDdHc2xNI

FOML ASSIGNMENT - YALLANKI.SUDHEER(211701061)
"""

import pandas as pd
file_path = "/content/SampleSuperstore.csv"
data = pd.read_csv(file_path)
data_info = data.info()
data_head = data.head()
data_info, data_head

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

data = pd.read_csv('SampleSuperstore.csv')

"""Linear Regression :"""

X_linear = data[['Quantity', 'Discount', 'Profit']]
y_linear = data['Sales']

X_train_linear, X_test_linear, y_train_linear, y_test_linear = train_test_split(X_linear, y_linear, test_size=0.2, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train_linear, y_train_linear)

y_pred_linear = linear_model.predict(X_test_linear)
mse_linear = mean_squared_error(y_test_linear, y_pred_linear)
print(f'Mean Squared Error for Linear Regression: {mse_linear}')

plt.figure(figsize=(10, 6))
plt.scatter(y_test_linear, y_pred_linear, alpha=0.5)
plt.plot([y_test_linear.min(), y_test_linear.max()], [y_test_linear.min(), y_test_linear.max()], 'r--', lw=2)
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Linear Regression: Predicted vs Actual Sales')
plt.grid(True)
plt.show()

"""Logistic Regression"""

data['Profitable'] = np.where(data['Profit'] > 0, 1, 0)
X_logistic = data[['Sales', 'Quantity', 'Discount']]
y_logistic = data['Profitable']

X_train_logistic, X_test_logistic, y_train_logistic, y_test_logistic = train_test_split(X_logistic, y_logistic, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_logistic = scaler.fit_transform(X_train_logistic)
X_test_logistic = scaler.transform(X_test_logistic)

logistic_model = LogisticRegression()
logistic_model.fit(X_train_logistic, y_train_logistic)

y_pred_logistic = logistic_model.predict(X_test_logistic)
accuracy_logistic = accuracy_score(y_test_logistic, y_pred_logistic)
print(f'Accuracy for Logistic Regression: {accuracy_logistic}')

conf_matrix = confusion_matrix(y_test_logistic, y_pred_logistic)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Logistic Regression: Confusion Matrix')
plt.show()

"""# Analysis Results:
# Linear Regression:
# The Mean Squared Error (MSE) for predicting "Sales" using "Quantity," "Discount," and "Profit" is approximately 680,377.46. A lower MSE indicates better model performance, so there's room for improvement in this model.

# Logistic Regression:
# The accuracy for predicting whether a sale is profitable or not based on "Sales," "Quantity," and "Discount" is 94.35%. This high accuracy suggests that the logistic regression model is performing well.
"""