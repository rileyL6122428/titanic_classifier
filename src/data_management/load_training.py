import csv

titanic_set_labelled = []

with open('/Users/rileylittlefield/Desktop/titanic_classifier/data/train.csv') as train_csv:
    reader = csv.DictReader(train_csv, delimiter=',')
    for row in reader:
        titanic_set_labelled.append(row)

print(titanic_set_labelled)
