"""
On trying the various models in deciding_model.ipynb, I found DecisionTreeClassifier gives 100% accuracy
(kinda sus)
So, here's the final model
"""
import numpy as np
import pandas as pd

dataset = pd.read_csv('music.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Feature-Scaling (standardization)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#DecisionTrees
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix is: ")
print(cm)
print(f"Accuracy score: {accuracy_score(y_test, y_pred)}")

import joblib

joblib.dump(clf, 'music-recommender.joblib')
joblib.dump(sc, 'standard-scaler.pkl')