from sklearn.metrics import precision_score, recall_score
from classifiers.k_neighbors_classifier.classifier import k_neighbors_classifier
from data_management.transformed_train_passengers import transformed_passengers as training_passengers
from data_management.X_Y import Y as survived

train_predictions = k_neighbors_classifier.predict(training_passengers)

print('precision =', precision_score(survived, train_predictions))
# ~0.93
print('recall =', recall_score(survived, train_predictions))
# ~0.81
