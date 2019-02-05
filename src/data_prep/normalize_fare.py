from data_management.fare_stats import max_fare, median_fare
import pdb

class NormalizeFare:

    def transform(self, passengers, survived=None):
        passengers.Fare = passengers.Fare.apply(lambda fare: self._normalize(fare))
        return passengers
    
    def fit_transform(self, passengers, survived=None):
        self.fit(passengers, survived)
        return self.transform(passengers, survived)

    def _normalize(self, fare):
        fare = fare if not fare and fare else median_fare
        return fare / max_fare
    
    def fit(self, passengers, survived=None):
        pass
    
