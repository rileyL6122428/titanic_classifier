from data_management.training_dataframe import passengers
from reusable_stats_builders.dispersion import print_dispersion_stats
from reusable_stats_builders.class_stats import print_class_stats

print('\n', 'PASSENGER FARE STATS', '\n')

has_fare = passengers[passengers.Fare != None]
print('HAS FARE LISTED COUNT =', len(has_fare), '\n')

print_dispersion_stats(
    passengers,
    'ALL',
    'Fare',
    units='UKNOWN'
)

print_dispersion_stats(
    passengers[passengers.Survived == '1'],
    'SURVIVED',
    'Fare',
    units='UKNOWN'
)

print_dispersion_stats(
    passengers[passengers.Survived == '0'],
    'UNSURVIVED',
    'Fare',
    units='UKNOWN'
)

range_limits = [0, 10, 20, 30, 50, 600]

for minimum, maximum in zip(range_limits, range_limits[1:]):
    print_class_stats(
        passengers[(passengers.Fare >= minimum) & (passengers.Fare < maximum)],
        'Survived',
        '1',
        ('BETWEEN (%s, %s)' % (minimum, maximum)),
    )
