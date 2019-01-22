from data_management.training_dataframe import passengers
from collections import Counter

print('TITLE STATS', '\n')

title_counter = Counter(passengers.Title)
print('Title Counts = ', title_counter, '\n')

def stats_by_title(titles, title_group_name):
    print(title_group_name, ' TITLE STATS', '\n')

    print('titles = ', titles, '\n')

    in_titles = passengers[passengers.Title.isin(titles)]
    survivors = in_titles[in_titles.Survived == '1']
    casualties = in_titles[in_titles.Survived == '0']

    print('Count = ', len(in_titles))
    print('Survivor Count = ', len(survivors))
    print('Casualty Count = ', len(casualties))
    print('Survivor Proportion = ', len(survivors) / len(in_titles), '\n')

stats_by_title(['Mr'], 'MR')
stats_by_title(['Miss', 'Ms', 'mlle'], 'MISS')
stats_by_title(['Mrs'], 'MRS')
stats_by_title([
    'Master',
    'Dr',
    '',
    'Rev',
    'Major',
    'Col',
    'Don',
    'Mme',
    'Lady',
    'Sir',
    'Capt',
    'Jonkheer'
], 'SPECIALIZED')
stats_by_title([
    'Major',
    'Col',
], 'MILITARY')
stats_by_title([
    'Mlle',
    'Don',
    'Mme',
    'Lady',
    'Sir',
    'Jonkheer'
], 'NOBILITY')
stats_by_title([
    'Master',
    'Dr',
], 'EDUCATED')
stats_by_title(['Capt'], 'CAPITAIN')
