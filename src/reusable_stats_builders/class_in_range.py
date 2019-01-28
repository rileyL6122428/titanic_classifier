from reusable_stats_builders.class_stats import print_class_stats

def print_class_across_range_stats(dataframe, attribute, range_limits, label_name, label_value):
    for minimum, maximum in zip(range_limits, range_limits[1:]):
        print_class_stats(
            dataframe[(dataframe[attribute] >= minimum) & (dataframe[attribute] < maximum)],
            label_name,
            label_value,
            ('BETWEEN (%s, %s)' % (minimum, maximum)),
        )
