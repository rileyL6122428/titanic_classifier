from data_management.pickers import count_passengers, is_any, pick_age
from data_management.load_training import titanic_set_labelled
from data_management.training_dataframe import passengers

print('STATS ON AGE', '\n')

print('LABELLED TOTAL = ', len(passengers), '\n')

missing_age = passengers[passengers.Age == '']

print('NUMBER OF PASSENGERS MISSING AGE = ', len(missing_age))
print('PROPORTION PASSENGERS MISSING AGE = ', round(len(missing_age) / len(passengers), 3), '\n')

having_age = passengers[passengers.Age != '']

print('NUMBER OF PASSENGERS WITH AGE = ', len(having_age))
print('PROPORTION PASSENGERS WITH AGE = ', round(len(having_age) / len(passengers), 3), '\n')

print('youngest age = ', having_age.Age.min())

print('oldest age = ', having_age.Age.max(), '\n')

# mean_age = sum(map(pick_age, having_age), 0) / having_age_count
# print('mean age = ', mean_age)

# median_age = (
#     (
#         pick_age(having_age_sorted[int(having_age_count /2)]) + 
#         pick_age(having_age_sorted[int(having_age_count / 2 - 1)])
#     ) / 2
# )
# print('median age = ', median_age)

