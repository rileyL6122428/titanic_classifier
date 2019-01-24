def print_class_stats(dataframe, label_name, label_value, stats_label=''):
    print(stats_label, 'CLASSIFICATION STATS', '\n')

    dataframe_target = dataframe[dataframe[label_name] == label_value]
    dataframe_not_target = dataframe[dataframe.Survived != label_value]

    print('total =', len(dataframe))
    print('in target count =', len(dataframe_target))
    print('not in target count =', len(dataframe_not_target), '' if len(dataframe) else '\n')
    
    if len(dataframe):
        print('proportion in target =', len(dataframe_target) / len(dataframe), '\n')
