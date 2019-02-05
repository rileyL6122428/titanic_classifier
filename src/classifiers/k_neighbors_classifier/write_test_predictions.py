from data_management.write_csv import write_csv
from classifiers.k_neighbors_classifier.classifier import k_neighbors_classifier
from data_management.transformed_test_passengers import transformed as test_passengers

# NEED TO NORMALIZE TO MAX FARE ACROSS TRAIN AND TEST
import pdb
pdb.set_trace()
predictions = k_neighbors_classifier.predict(test_passengers)

ids = range(892, 1310)

write_csv(
    file_path='/Users/rileylittlefield/Desktop/titanic_classifier/data/neighbor_predictions.csv',
    headers=['PassengerId', 'Survived'],
    rows=zip(ids, predictions)
)
