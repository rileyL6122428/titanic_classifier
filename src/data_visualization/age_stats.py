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

print('SURVIVOR DISPERSION', '\n')

survivors = having_age[having_age.Survived == '1']
print('youngest age = ', survivors.Age.min())
print('oldest age = ', survivors.Age.max())
print('mean age = ', survivors.Age.mean(), '\n')

print('first quartile = ', survivors.Age.quantile(.25))
print('median = ', survivors.Age.median())
print('third quartile = ', survivors.Age.quantile(.75), '\n')

print('CASUALTY DISPERSION', '\n')

casualities = having_age[having_age.Survived == '0']
print('youngest age = ', casualities.Age.min())
print('oldest age = ', casualities.Age.max())
print('mean age = ', casualities.Age.mean(), '\n')

print('first quartile = ', casualities.Age.quantile(.25))
print('median age = ', casualities.Age.median())
print('third quartile = ', casualities.Age.quantile(.75), '\n')
