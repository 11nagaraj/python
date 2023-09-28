import numpy as np
import matplotlib.pyplot as plt

# Define the number of values
num_values = 1000

# Define the frequency of the cosine wave
frequency = 5

# Define the time values from 0 to 2*pi
time = np.linspace(0, 2 * np.pi, num_values)

# Generate the cosine series
cosine_series = np.cos(frequency * time)

# Plot the cosine series
plt.plot(time, cosine_series)
plt.title('Cosine Series')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
