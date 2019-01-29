class GCFTransformer:

    def transform(self, passengers, survived=None):
        return passengers.drop(columns=[
            'PassengerId',
            'Name',
            'Age',
            'SibSp',
            'Parch',
            'Ticket',
            'Cabin',
            'Embarked',
            'Title'
        ])
