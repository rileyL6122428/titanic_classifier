from collections import Counter

def print_dispersion_stats(dataframe, stats_title, attribute, units=''):
    print(stats_title, 'DISPERSION STATS', '\n')

    if units:
        print('Stats below are in', units, '\n')
    
    series = dataframe[attribute]

    print('counts =', Counter(series), '\n')

    print('MIN =', series.min())
    print('MAX =', series.max(), '\n')
    
    print('MEAN - STD =', series.mean() - series.std())
    print('MEAN =', series.mean())
    print('MEAN + STD =', series.mean() + series.std(), '\n')

    print('15% quantile =', series.quantile(.15))
    print('50% quantile =', series.median())
    print('85% quantile =', series.quantile(.85), '\n')
