from data_management.training_dataframe import passengers
from functools import reduce

print('STATS ON SEX', '\n')

print('TOTAL LABELLED ENTRIES: ', len(passengers), '\n')

male_passengers = passengers[passengers.Sex == 'male']
print('TOTAL MALES = ', len(male_passengers))

surviving_males = male_passengers[male_passengers.Survived == '1']
print('SURVIVING MALES = ', len(surviving_males))

surviving_male_ratio = len(surviving_males) / len(male_passengers)
print('SURVIVING MALES RATIO = ', round(surviving_male_ratio, 3), '\n')

female_passengers = passengers[passengers.Sex == 'female']
print('TOTAL FEMALES = ', len(female_passengers))

surviving_females = female_passengers[female_passengers.Survived == '1']
print('TOTAL SURVIVING FEMALES = ', len(surviving_females))

surviving_female_ratio = len(surviving_females) / len(female_passengers)
print('SURVIVING FEMALES RATIO = ', round(surviving_female_ratio, 3), '\n')
