from data_management.training_dataframe import passengers
from sklearn.linear_model import LogisticRegression
from data_management.X_Y import X as passengers, Y as survived 
from data_prep.pipelines import passenger_transformer
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import GridSearchCV

transformed = passenger_transformer.transform(passengers)

grid_search_logistic = GridSearchCV(
    cv=5,
    estimator=LogisticRegression(),
    param_grid=[
        {
            'solver': [ 'sag', 'lbfgs' ],
            'max_iter': [ 100 ],
            'C': [ 0.7, 0.8, 1.0 ],
            'tol': [0.0001, 0.00001]
        }
    ],
    verbose=10,
    n_jobs=2,
    scoring="f1"
)

grid_search_logistic.fit(transformed, survived)

print('best params =', grid_search_logistic.best_params_)

logistic_classifier = grid_search_logistic.best_estimator_

predictions = logistic_classifier.predict(transformed)

print('precision =', precision_score(survived, predictions))
# ~.74
print('recall =', recall_score(survived, predictions))
# ~.69
