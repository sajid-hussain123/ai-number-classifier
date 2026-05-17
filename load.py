import pandas as pd

df = pd.read_csv("numbers.csv")

print(df.head())

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X = df[["Number"]]
y = df["Category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print(predictions)

import pandas as pd

new_data = pd.DataFrame({"Number": [9912345678]})

new_prediction = clf.predict(new_data)

print(new_prediction)