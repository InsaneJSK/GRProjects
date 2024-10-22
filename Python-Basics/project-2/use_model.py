import joblib
clf = joblib.load('music-recommender.joblib')
sc = joblib.load('standard-scaler.pkl')

age = int(input("Enter your age: "))
gender = int(input("Enter 0 for female and 1 for male: "))

print(clf.predict(sc.transform([[age, gender]])))