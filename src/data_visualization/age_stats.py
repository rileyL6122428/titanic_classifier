from data_management.pickers import count_passengers, is_any, pick_age
from data_management.load_training import titanic_set_labelled

print('STATS ON AGE', '\n')

passenger_count = count_passengers(is_any)
print('LABELLED TOTAL = ', passenger_count, '\n')

missing_age = [
    passenger
    for passenger
    in titanic_set_labelled
    if not passenger['Age']
]

missing_age_count = len(missing_age)

having_age = [
    passenger
    for passenger
    in titanic_set_labelled
    if passenger['Age']
]

having_age_count = len(having_age)

print('NUMBER OF PASSENGERS MISSING AGE = ', missing_age_count)
print('PROPORTION PASSENGERS MISSING AGE = ', round(missing_age_count / passenger_count, 3), '\n')

print('NUMBER OF PASSENGERS WITH AGE = ', having_age_count)
print('PROPORTION PASSENGERS WITH AGE = ', round(having_age_count / passenger_count, 3), '\n')

youngest_passenger = min(having_age, key=pick_age)
print('youngest age = ', youngest_passenger['Age'])

oldest_passenger = max(having_age, key=pick_age)
print('oldest age = ', oldest_passenger['Age'], '\n')

mean_age = sum(map(pick_age, having_age), 0) / having_age_count
print('mean age = ', mean_age)
