from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import GridSearchCV
from data_management.X_Y import Y as survived
from data_management.transformed_train_passengers import transformed_passengers as training_passengers

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

grid_search_neighbors.fit(training_passengers, survived)

# print('best params =', grid_search_neighbors.best_params_)
# best params = {'n_neighbors': 5, 'p': 1, 'weights': 'distance'}

k_neighbors_classifier = grid_search_neighbors.best_estimator_
