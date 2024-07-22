import numpy as np
import time
import sys

def calculate_correlation(time_series1, time_series2):
    correlation = np.corrcoef(time_series1, time_series2)[0, 1]
    return correlation

def main():
    time_series1 = np.load('data/time_series1.npy')
    time_series2 = np.load('data/time_series2.npy')

    time1 = time.time()
    jobs = [(i, j) for i in range(time_series1.shape[0]) for j in range(time_series2.shape[0])]
    job_indxs = jobs[sys.argv[1]]

    correlation = calculate_correlation(time_series1[job_indxs[0]], time_series2[job_indxs[1]])
    print(f'Correlation between series 1 | {job_indxs[0]} and series 2 | {job_indxs[1]}:', correlation, flush=True)
    time2 = time.time()
    print('Time taken:', time2 - time1, flush=True)