from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from data_prep.pipelines import passenger_transformer
from data_management.X_Y import X as passengers, Y as survived

transformed_passengers = passenger_transformer.transform(passengers)

grid_search_rfc = GridSearchCV(
    estimator=RandomForestClassifier(),
    param_grid=[
        { 
            'n_estimators': [10, 100],
            'max_features': [None, 2, 3, 4, 5, 6],
            'random_state': [43]
        }
    ],
    scoring='f1'
)

grid_search_rfc.fit(transformed_passengers, survived)

print('best params =', grid_search_rfc.best_params_)
# {'max_features': 5, 'n_estimators': 100, 'random_state': 43}

rfc_classifer = grid_search_rfc.best_estimator_

predictions = rfc_classifer.predict(transformed_passengers)

print('precision score =', precision_score(survived, predictions))
# 0.92
print('recall score =', recall_score(survived, predictions))
# 0.82
