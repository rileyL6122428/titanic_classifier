from collections import Counter

def print_dispersion_stats(dataframe, stats_title, attribute, units='', show_counts=False):
    print(stats_title, 'DISPERSION STATS', '\n')

    if units:
        print('Stats below are in', units, '\n')
    
    series = dataframe[attribute]

    print('COUNT =', len(series), '\n')

    print('MIN =', series.min())
    print('MAX =', series.max(), '\n')
    
    if len(series):
        print('MEAN - STD =', series.mean() - series.std())
        print('MEAN =', series.mean())
        print('MEAN + STD =', series.mean() + series.std(), '\n')

    print('15% quantile =', series.quantile(.15))
    print('50% quantile =', series.median())
    print('85% quantile =', series.quantile(.85), '\n')

    if show_counts:
        print('counts =', Counter(series), '\n')