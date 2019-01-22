from data_management.training_dataframe import passengers
from reusable_stats_builders.dispersion import print_dispersion_stats

print_dispersion_stats(passengers, 'PARENT CHILD COUNT', 'Parch', units='Persons')

print_dispersion_stats(
    passengers[passengers.Survived == '1'],
    'SURVIVED PARENT CHILD COUNT',
    'Parch',
    units='Persons'
)

print_dispersion_stats(
    passengers[passengers.Survived == '0'],
    'CASUALTY PARENT CHILD COUNT',
    'Parch',
    units='Persons'
)
