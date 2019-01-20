from data_management.load_training import titanic_set_labelled
from data_management.training_dataframe import passengers

print('STATS ON AGE', '\n')

print('LABELLED TOTAL = ', len(passengers), '\n')

missing_age = passengers[passengers.Age == '']

print('NUMBER OF PASSENGERS MISSING AGE = ', len(missing_age))
print('PROPORTION PASSENGERS MISSING AGE = ', round(len(missing_age) / len(passengers), 3), '\n')

having_age = passengers[passengers.Age != '']

print('NUMBER OF PASSENGERS WITH AGE = ', len(having_age))
print('PROPORTION PASSENGERS WITH AGE = ', round(len(having_age) / len(passengers), 3), '\n')


print('youngest age = ', having_age.Age.min())
print('oldest age = ', having_age.Age.max())
print('mean age = ', having_age.Age.mean(), '\n')

print('1st quartile = ', having_age.Age.quantile(.25))
print('median age = ', having_age.Age.median())
print('3rd quartile = ', having_age.Age.quantile(.75), '\n')

