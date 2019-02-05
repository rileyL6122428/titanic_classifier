from sklearn.pipeline import Pipeline
from data_prep.drop_attrs import DropAttrsTransformer
from data_prep.one_hot_encode_gender import OneHotEncodeGender
from data_prep.normalize_fare import NormalizeFare
from data_prep.one_hot_encode_class import PassengerClassEncoder

passenger_transformer = Pipeline(steps=[

    ('encode_gender', OneHotEncodeGender(sparse=False)),
    ('encode_class', PassengerClassEncoder(sparse=False)),
    ('normalize_fare', NormalizeFare()),
    ('drop_attrs', DropAttrsTransformer(attrs=[
        'PassengerId',
        'Name',
        'Age',
        'SibSp',
        'Parch',
        'Ticket',
        'Cabin',
        'Embarked',
        'Title'
    ])),
])
