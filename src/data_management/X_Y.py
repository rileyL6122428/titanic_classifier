from data_management.training_dataframe import passengers

Y = passengers.Survived.map({ '0': 0, '1': 1 })
X = passengers.drop(columns=['Survived'])
