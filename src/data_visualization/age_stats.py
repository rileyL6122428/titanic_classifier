from data_management.load_training import titanic_set_labelled
from data_management.training_dataframe import passengers
from reusable_stats_builders.dispersion import print_dispersion_stats

print('STATS ON AGE', '\n')

print('LABELLED TOTAL = ', len(passengers), '\n')

missing_age = passengers[passengers.Age == '']

print('NUMBER OF PASSENGERS MISSING AGE = ', len(missing_age))
print('PROPORTION PASSENGERS MISSING AGE = ', round(len(missing_age) / len(passengers), 3), '\n')

having_age = passengers[passengers.Age != '']
print('NUMBER OF PASSENGERS WITH AGE = ', len(having_age))
print('PROPORTION PASSENGERS WITH AGE = ', round(len(having_age) / len(passengers), 3), '\n')
print_dispersion_stats(having_age, 'AGE POPULATED', 'Age', 'YRs')


survivors = having_age[having_age.Survived == '1']
print_dispersion_stats(survivors, 'SURVIVOR AGES', 'Age', 'YRs')

casualities = having_age[having_age.Survived == '0']
print_dispersion_stats(casualities, 'CASUALTY AGES', 'Age', 'YRs')
