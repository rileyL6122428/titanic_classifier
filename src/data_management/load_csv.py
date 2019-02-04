import csv

titanic_set_labelled = []


def load_titanic_csv(file_path):
    csv_list = []

    with open(file_path) as target_csv:
        reader = csv.DictReader(target_csv, delimiter=',')
        for row in reader:
            csv_list.append(row)
    
    return csv_list
