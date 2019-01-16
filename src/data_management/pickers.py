from data_management.load_training import titanic_set_labelled
from functools import reduce

def count_passengers(criteria):
    return reduce(
        lambda agg, passenger: agg + (1 if criteria(passenger) else 0),
        titanic_set_labelled,
        0
    )

def is_any(passenger):
    return True

def is_male(passenger):
    return passenger['Sex'] == 'male'


def is_female(passenger):
    return passenger['Sex'] == 'female'


def survived(passenger):
    return passenger['Survived'] == '1'

def pick_age(passenger):
    return float(passenger['Age'])