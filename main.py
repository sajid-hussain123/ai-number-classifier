import random
import csv

categories = [
    ('99', 'family'),
    ('88', 'friends'),
    ('77', 'spam'),
    ('66', 'office')
]

data = []
for prefix, label in categories:
    for _ in range(25):  # Adjust the number as needed
        number = prefix + ''.join(random.choices('0123456789', k=8))
        data.append((number, label))

with open('numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Number', 'Category'])
    writer.writerows(data)


    import pandas as pd

df = pd.read_csv("numbers.csv")

print(df.head())