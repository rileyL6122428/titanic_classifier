from data_management.X_Y import X, Y
import pandas
from sklearn.preprocessing import OneHotEncoder

class PassengerClassEncoder:

    def __init__(self, sparse=False):
        self.encoder = OneHotEncoder(sparse=False)
    
    def transform(self, passengers, survived=None):
        wrapped_pclasses = list(map(lambda pclass: [pclass], passengers.Pclass))
        encoded_pclasses = self.encoder.fit_transform(wrapped_pclasses)
        encoded_pclasses_df = pandas.DataFrame(
            encoded_pclasses,
            columns=[
                'first_class',
                'second_class',
                'third_class'
            ]
        )
        passengers = pandas.concat([passengers, encoded_pclasses_df], axis=1)
        return passengers.drop(columns=['Pclass'])


 
