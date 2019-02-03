from data_management.X_Y import X as passengers, Y as survived

class NormalizeFare:

    def transform(self, passengers, survived=None):
        max_fare = passengers.Fare.max()
        passengers.Fare = passengers.Fare.apply(lambda fare: fare / max_fare)
        return passengers
    
    def fit_transform(self, passengers, survived=None):
        self.fit(passengers, survived)
        return self.transform(passengers, survived)
    
    def fit(self, passengers, survived=None):
        pass
    