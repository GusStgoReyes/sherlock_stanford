import numpy as np
import time

def calculate_correlation(time_series1, time_series2):
    correlation = np.corrcoef(time_series1, time_series2)[0, 1]
    return correlation

def main():
    time_series1 = np.load('data/time_series1.npy')
    time_series2 = np.load('data/time_series2.npy')

    time1 = time.time()
    max_correlation, indxs = 0, (None, None)
    for i in range(time_series1.shape[0]):
        for j in range(time_series2.shape[0]):
            correlation = calculate_correlation(time_series1[i], time_series2[j])
            if np.abs(correlation) > max_correlation:
                max_correlation = correlation
                indxs = (i, j)
            print(f'Correlation between series 1 | {i} and series 2 | {j}:', correlation, flush=True)
    time2 = time.time()
    print('Max correlation:', max_correlation, flush=True)
    print('Indexes:', indxs, flush=True)