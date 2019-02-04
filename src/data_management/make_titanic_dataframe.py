from pandas import DataFrame
import re


def adapt_age(age):
    return float(age) if age else age


def parse_title(name):
    parsed = re.search(', (\w+)\.', name)
    return parsed[0][2:-1] if parsed else ''


def parse_sibsp(count):
    return int(count)


def parse_parch(count):
    return int(count)


def parse_fare(fare):
    return float(fare) if fare else None


def as_dataframe(titanic_set):
    as_columns = {
        column_name: []
        for column_name
        in titanic_set[0].keys()
    }

    as_columns['Title'] = []

    for passenger in titanic_set:
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
            elif col_name == 'Cabin':
                as_columns.get('Cabin').append(value)
            elif col_name == 'Fare':
                as_columns.get('Fare').append(parse_fare(value))
            else:
                as_columns.get(col_name).append(value)

    return DataFrame(data=as_columns)
