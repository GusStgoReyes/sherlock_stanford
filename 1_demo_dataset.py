import numpy as np

# Create random time series data
elements1 = 10
elements2 = 20
time_points = 450
correlated_indx1 = np.random.choice(elements1, 1, replace=False)[0]
correlated_indx2 = np.random.choice(elements2, 1, replace=False)[0]

# Correlated signal
x = np.linspace(-np.pi, np.pi, time_points)
signal = np.sin(x)

# Random time series
time_series1 = np.random.rand(elements1, time_points)
time_series2 = np.random.rand(elements2, time_points)

# Add correlated signal to the time series  
time_series1[correlated_indx1] = time_series1[correlated_indx1] + signal
time_series2[correlated_indx2] = time_series2[correlated_indx2] + signal

# Save the time series data
np.save('data/time_series1.npy', time_series1)
np.save('data/time_series2.npy', time_series2)