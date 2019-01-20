from pandas import DataFrame
from data_management.load_training import titanic_set_labelled

as_columns = {
    column_name: []
    for column_name
    in titanic_set_labelled[0].keys()
}

def adapt_age(age):
    return float(age) if age else age

for passenger in titanic_set_labelled:
    for col_name, value in passenger.items():
        if col_name == 'Age':
            as_columns.get(col_name).append(adapt_age(value))
        else:
            as_columns.get(col_name).append(value)

passengers = DataFrame(data=as_columns)

# ages = passengers.Age

# not_having_age = passengers[passengers.Age == '']
# having_age = passengers[passengers.Age != '']
# print(len(having_age))
# print(len(not_having_age))