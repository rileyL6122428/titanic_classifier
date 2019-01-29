from data_management.X_Y import X as passengers, Y as survived

class NormalizeFare:

    def transform(self, passengers, survived=None):
        max_fare = passengers.Fare.max()
        passengers.Fare = passengers.Fare.apply(lambda fare: fare / max_fare)
        return passengers
