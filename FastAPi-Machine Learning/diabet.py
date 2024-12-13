from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle 

# Veriyi oku
df = pd.read_csv("diabetes.csv", encoding="utf-8")

# Hedef değişken ve özellikleri ayır
y = df['Outcome']
x = df.drop(['Outcome'], axis=1)

# Veriyi eğitim ve test setlerine ayır
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

# KNN Modeli
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(x_train.values, y_train)
X = [[8, 65, 72, 23, 0, 32, 0.6, 42]]
print("KNN Predict:", knn.predict(X))
print("KNN Score:", knn.score(x_test, y_test))

# Logistic Regression Modeli
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(x_train.values, y_train)
print("Logistic Regression Predict:", log_reg.predict(X))
print("Logistic Regression Score:", log_reg.score(x_test, y_test))

# Decision Tree Modeli
dec_tree = DecisionTreeClassifier()
dec_tree.fit(x_train.values, y_train)
print("Decision Tree Predict:", dec_tree.predict(X))
print("Decision Tree Score:", dec_tree.score(x_test, y_test))

# Modelleri kaydet
with open('knn.sav', 'wb') as f:
    pickle.dump(knn, f)
with open('log_reg.sav', 'wb') as f:
    pickle.dump(log_reg, f)
with open('dec_tree.sav', 'wb') as f:
    pickle.dump(dec_tree, f)

print("Modeller kaydedildi")
