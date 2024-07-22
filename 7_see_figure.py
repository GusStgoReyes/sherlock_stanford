import matplotlib.pyplot as plt

# Sample data
time = [1, 2, 3, 4, 5]
signal = [10, 15, 12, 17, 14]

# Plotting the time series signal
plt.plot(time, signal)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Time Series Signal')
plt.show()