from collections import Counter

def print_dispersion_stats(dataframe, stats_title, attribute):
    print(stats_title, ' STATS', '\n')
    
    series = dataframe[attribute]

    counts = Counter(series)
    print('counts = ', counts, '\n')

    min_val = series.min()
    print('MIN = ', min_val)
    max_val = series.max()
    print('MAX = ', max_val, '\n')
    
    mean_minus_std = series.mean() - series.std()
    print('MEAN - STD = ', mean_minus_std)
    mean = series.mean()
    print('MEAN = ', mean)
    mean_plus_std = series.mean() + series.std()
    print('MEAN + STD = ', mean_plus_std, '\n')

    fifteen_quantile = series.quantile(.15)
    print('15% quantile = ', fifteen_quantile)
    median = series.median()
    print('50% quantile = ', median)
    eighty_five_quantile = series.quantile(.85)
    print('85% quantile = ', eighty_five_quantile, '\n')
