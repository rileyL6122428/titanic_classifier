class DropAttrsTransformer:

    def __init__(self, attrs=[]):
        self.attrs = attrs

    def transform(self, passengers, survived=None):
        return passengers.drop(columns=self.attrs)
    
    def fit_transform(self, passengers, survived=None):
        return self.transform(passengers, survived)

    def fit(self, passengers, survived=None):
        pass