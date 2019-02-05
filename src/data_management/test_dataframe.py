from data_management.load_test import titanic_test_set
from data_management.make_titanic_dataframe import as_dataframe

passengers = as_dataframe(titanic_test_set)
