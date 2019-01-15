from data_management.load_training import titanic_set_labelled
from functools import reduce

print('STATS ON SEX')

labelled_total = len(titanic_set_labelled)
print('TOTAL LABELLED ENTRIES: ', labelled_total)
# 891

row_labels = titanic_set_labelled[0].keys()
print('ATTRIBUTES: ', row_labels)
# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

def count_passengers(criteria):
    return reduce(
        lambda agg, passenger: agg + (1 if criteria(passenger) else 0),
        titanic_set_labelled,
        0
    )

def is_male(passenger):
    return passenger['Sex'] == 'male'

def is_female(passenger):
    return passenger['Sex'] == 'female'

def survived(passenger):
    return passenger['Survived'] == '1'

male_count = count_passengers(is_male)
print('TOTAL MALES = ', male_count)

surviving_males = count_passengers(lambda passenger: is_male(passenger) and survived(passenger))
print('SURVIVING MALES = ', surviving_males)

female_count = count_passengers(is_female)
print('TOTAL FEMALES = ', female_count)
