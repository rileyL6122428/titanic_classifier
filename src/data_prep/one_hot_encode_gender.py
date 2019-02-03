from sklearn.preprocessing import OneHotEncoder
from data_management.X_Y import passengers
import pandas as pd

class OneHotEncodeGender:

    def __init__(self, sparse=False):
        self.encoder_ = OneHotEncoder(sparse=sparse)

    def transform(self, passengers, survived=None):
        wrapped_genders = self._wrap_genders(passengers)
        encoded_genders = self.encoder_.fit_transform(wrapped_genders)
        encoded_genders_dataframe = pd.DataFrame(
            encoded_genders,
            columns=[
                'female',
                'male'
            ]
        )
        return (pd
            .concat([passengers, encoded_genders_dataframe], axis=1)
            .drop(columns=['Sex'])
        )
    
    def fit_transform(self, passengers, survived=None):
        self.fit(passengers, survived)
        return self.transform(passengers)
    
    def fit(self, passengers, survived=None):
        pass
    
    def _wrap_genders(self, passengers):
        return list(map(lambda pclass: [pclass], passengers.Sex))
