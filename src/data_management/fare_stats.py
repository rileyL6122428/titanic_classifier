from data_management.test_dataframe import passengers as test_passengers
from data_management.training_dataframe import passengers as train_passengers
import pandas as pd

joined_passengers = pd.concat([test_passengers, train_passengers])

max_fare = joined_passengers.Fare.max()
median_fare = joined_passengers.Fare.median()