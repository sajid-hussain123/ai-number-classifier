import pandas as pd
from flask import Flask, request, render_template
df = pd.read_csv("numbers.csv")

print(df.head())

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X = df[["Number"]]
y = df["Category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    number = float(request.form['number'])

    new_data = pd.DataFrame({"Number": [number]})

    category = clf.predict(new_data)[0]

    return f'Developed by Sajid. The Enter Mobile number is classified as : {category}'

if __name__ == '__main__':
    app.run(debug=True)