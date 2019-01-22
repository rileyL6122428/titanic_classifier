from data_management.training_dataframe import passengers
from collections import Counter

print('Passenger Class Stats', '\n')

class_counts = Counter(passengers.Pclass)
print('Passenger Class Counts = ', class_counts, '\n')

print('CLASS 1 STATS', '\n')

class_1 = passengers[passengers.Pclass == '1']
class_1_surviors = class_1[class_1.Survived == '1']
class_1_casualties = class_1[class_1.Survived == '0']

print('Count = ', len(class_1))
print('Survivor Count = ', len(class_1_surviors))
print('Casualty Count = ', len(class_1_casualties))
print('Survivor Proportion = ', len(class_1_surviors) / len(class_1), '\n')

print('CLASS 2 STATS', '\n')

class_2 = passengers[passengers.Pclass == '2']
class_2_survivors = class_2[class_2.Survived == '1']
class_2_casualties = class_2[class_2.Survived == '0']

print('Count = ', len(class_2))
print('Survivor Count = ', len(class_2_survivors))
print('Casualty Count = ', len(class_2_casualties))
print('Survivor Proportion = ', len(class_2_survivors) / len(class_2), '\n')

print('CLASS 3 STATS', '\n')

class_3 = passengers[passengers.Pclass == '3']
class_3_survivors = class_3[class_3.Survived == '1']
class_3_casualties = class_3[class_3.Survived == '0']

print('Count = ', len(class_3))
print('Survivor Count = ', len(class_3_survivors))
print('Casualty Count = ', len(class_3_casualties))
print('Survivor Proportion = ', len(class_3_survivors) / len(class_3))
