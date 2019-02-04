from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import GridSearchCV
from data_management.X_Y import X as passengers, Y as survived
from data_prep.pipelines import passenger_transformer


transformed_passengers = passenger_transformer.transform(passengers)

grid_search_neighbors = GridSearchCV(
    cv = 5,
    estimator = KNeighborsClassifier(),
    param_grid = [
        {
            'n_neighbors': [3, 4, 5],
            'weights': ['distance', 'uniform'],
            'p': [1, 2]
        }
    ],
    scoring = 'f1',
    verbose=10
)

grid_search_neighbors.fit(transformed_passengers, survived)

print('best params =', grid_search_neighbors.best_params_)

classifier = grid_search_neighbors.best_estimator_

predictions = classifier.predict(transformed_passengers)

print('precision =', precision_score(survived, predictions))
# ~0.93
print('recall =', recall_score(survived, predictions))
# ~0.81
