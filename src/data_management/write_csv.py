import csv

file_path = '/Users/rileylittlefield/Desktop/titanic_classifier/data/neighbor_predictions.csv'

def write_csv(file_path, headers=[], rows=[]):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='|',
            quoting=csv.QUOTE_MINIMAL
        )

        writer.writerow(headers)

        for row in rows:
            writer.writerow(row)
