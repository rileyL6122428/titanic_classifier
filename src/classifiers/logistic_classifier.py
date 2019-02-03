from data_management.training_dataframe import passengers
from sklearn.linear_model import LogisticRegression
from data_management.X_Y import X as passengers, Y as survived 
from data_prep.pipelines import passenger_transformer
from sklearn.metrics import precision_score, recall_score

transformed = passenger_transformer.transform(passengers)

logistic_classifier = LogisticRegression(
    solver='sag',
    max_iter=100,
    C=1.0,
    tol=0.0001
)

logistic_classifier.fit(transformed, survived)

# print('transformed')
# print(transformed[:8])

predictions = logistic_classifier.predict(transformed)

# for (actual, prediction) in zip(survived[:20], predictions_first_20):
#     print('prediction =', prediction, ', actual =', actual)

print('precision =', precision_score(survived, predictions))
# ~.74
print('recall =', recall_score(survived, predictions))
# ~.69
