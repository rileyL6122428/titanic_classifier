from data_management.training_dataframe import passengers
from reusable_stats_builders.class_stats import print_class_stats
from collections import Counter
import re

print('CABIN STATS', '\n')

without_cabin_label = passengers[passengers.Cabin == '']
print('WITHOUT CABIN LABEL =', len(without_cabin_label))

with_cabin_label = passengers[passengers.Cabin != '']
print('WITH CABIN LABEL =', len(with_cabin_label))

print('PROPORTION WITH CABIN LABEL =', len(with_cabin_label) / len(passengers), '\n')

print_class_stats(
    without_cabin_label,
    label_name='Survived',
    label_value='1',
    stats_label='NOT HAVING CABIN LABEL'
)

print_class_stats(
    with_cabin_label,
    label_name='Survived',
    label_value='1',
    stats_label='HAVING CABIN LABEL'
)

def extract_labels(cabin_labels_string):
    return list(set(re.findall('[a-zA-Z]', cabin_labels_string)))

cabin_labels = [
    label
    for labels in with_cabin_label.Cabin
    for label in extract_labels(labels)
]

print('LABEL COUNTS =', Counter(cabin_labels), '\n')

for label in Counter(cabin_labels).keys():
    print_class_stats(
        with_cabin_label[
            with_cabin_label.Cabin.apply(lambda labels: label in extract_labels(labels))
        ],
        label_name='Survived',
        label_value='1',
        stats_label=('HAVING CABIN LABEL IN %s SECTION' % label)
    )
