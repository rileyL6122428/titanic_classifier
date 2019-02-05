from data_management.X_Y import X as passengers, Y as survived
from data_prep.pipelines import passenger_transformer

transformed_passengers = passenger_transformer.transform(passengers)
