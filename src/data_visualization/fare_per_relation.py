from data_management.training_dataframe import passengers
from reusable_stats_builders.dispersion import print_dispersion_stats
from reusable_stats_builders.class_in_range import print_class_across_range_stats

print( '\n', 'FARE PER RELATION STATS', '\n')

fare_per_relation = passengers['Fare'] / (passengers['Parch'] + passengers['SibSp'] + 1)

passengers['FarePerRelation'] = fare_per_relation

print_dispersion_stats(
    passengers,
    'FARE PER RELATION',
    'FarePerRelation',
)

range_limits = [0, 10, 15, 600]

print_class_across_range_stats(
    dataframe=passengers,
    attribute='FarePerRelation',
    range_limits=range_limits,
    label_name='Survived',
    label_value='1'
)
