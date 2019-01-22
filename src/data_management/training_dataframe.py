from pandas import DataFrame
from data_management.load_training import titanic_set_labelled
import re

as_columns = {
    column_name: []
    for column_name
    in titanic_set_labelled[0].keys()
}

as_columns['Title'] = []

def adapt_age(age):
    return float(age) if age else age

def parse_title(name):
    parsed = re.search(', (\w+)\.', name)
    return parsed[0][2:-1] if parsed else ''

def parse_sibsp(count):
    return int(count)

def parse_parch(count):
    return int(count)

for passenger in titanic_set_labelled:
    for col_name, value in passenger.items():
        if col_name == 'Age':
            as_columns.get(col_name).append(adapt_age(value))
        elif col_name == 'Name':
            as_columns.get(col_name).append(value)
            as_columns.get('Title').append(parse_title(value))
        elif col_name == 'SibSp':
            as_columns.get('SibSp').append(parse_sibsp(value))
        elif col_name == 'Parch':
            as_columns.get('Parch').append(parse_parch(value))
        else:
            as_columns.get(col_name).append(value)

passengers = DataFrame(data=as_columns)

# ages = passengers.Age

# not_having_age = passengers[passengers.Age == '']
# having_age = passengers[passengers.Age != '']
# print(len(having_age))
# print(len(not_having_age))
