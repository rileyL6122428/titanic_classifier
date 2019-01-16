from data_management.pickers import count_passengers, is_male, is_female, survived, is_any
from functools import reduce

print('STATS ON SEX', '\n')

labelled_total = count_passengers(is_any)
print('TOTAL LABELLED ENTRIES: ', labelled_total, '\n')

male_count = count_passengers(is_male)
print('TOTAL MALES = ', male_count)

surviving_males = count_passengers(lambda passenger: is_male(passenger) and survived(passenger))
print('SURVIVING MALES = ', surviving_males)

surviving_male_ratio = surviving_males / male_count
print('SURVIVING MALES RATIO = ', round(surviving_male_ratio, 3), '\n')

female_count = count_passengers(is_female)
print('TOTAL FEMALES = ', female_count)

surviving_female_count = count_passengers(lambda passenger: is_female(passenger) and survived(passenger))
print('TOTAL SURVIVING FEMALES = ', surviving_female_count)

surviving_female_ratio = surviving_female_count / female_count
print('SURVIVING FEMALES RATIO = ', round(surviving_female_ratio, 3), '\n')
