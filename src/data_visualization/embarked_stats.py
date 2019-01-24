from data_management.training_dataframe import passengers
from collections import Counter
from reusable_stats_builders.class_stats import print_class_stats

print('\n', 'LOCATION EMBARKED STATS BELOW', '\n')

print('KEY')
print('C = Cherbourg')
print('Q = Queenstown')
print('S = Southampton', '\n')

# { 'C', 'Q', 'S' }



print('LOCATION COUNTS:', Counter(passengers.Embarked), '\n')

for location, abbreviated in [('Cherbourg', 'C'), ('Queenstown', 'Q'), ('Southampton', 'S')]:
    print_class_stats(
        passengers[passengers.Embarked == abbreviated], 
        'Survived',
        '1',
        stats_label=('%s' % (location.upper()))
    )    
