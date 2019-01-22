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

print('SURVIVOR DISPERSION', '\n')

survivors = having_age[having_age.Survived == '1']
print('youngest age = ', survivors.Age.min())
print('oldest age = ', survivors.Age.max(), '\n')

print('mean - std = ', survivors.Age.mean() - survivors.Age.std())
print('mean age = ', survivors.Age.mean())
print('mean + std = ', survivors.Age.mean() + survivors.Age.std(), '\n')

print('15 percent quantile = ', survivors.Age.quantile(.15))
print('median = ', survivors.Age.median())
print('85 percent quantile = ', survivors.Age.quantile(.85), '\n')

print('CASUALTY DISPERSION', '\n')

casualities = having_age[having_age.Survived == '0']
print('youngest age = ', casualities.Age.min())
print('oldest age = ', casualities.Age.max(), '\n')

print('mean age - std age = ', casualities.Age.mean() - casualities.Age.std())
print('mean age = ', casualities.Age.mean())
print('mean age + std age = ', casualities.Age.mean() + casualities.Age.std(), '\n')

print('15 percent quantile = ', casualities.Age.quantile(.15))
print('median age = ', casualities.Age.median())
print('85 percent quantile = ', casualities.Age.quantile(.85), '\n')
