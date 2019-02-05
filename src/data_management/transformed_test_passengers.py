from data_prep.pipelines import passenger_transformer
from data_management.test_dataframe import passengers

transformed = passenger_transformer.transform(passengers)