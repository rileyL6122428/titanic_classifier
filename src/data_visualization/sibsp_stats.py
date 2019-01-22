from data_management.training_dataframe import passengers
from reusable_stats_builders.dispersion import print_dispersion_stats

print_dispersion_stats(passengers, 'SIBLING SPOUSE COUNT', 'SibSp')
