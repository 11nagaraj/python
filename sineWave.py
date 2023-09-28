import numpy as np
import matplotlib.pyplot as plt

# Define the number of values
num_values = 1000

# Define the frequency of the sine wave
frequency = 5

# Define the time values from 0 to 2*pi
time = np.linspace(0, 2 * np.pi, num_values)

# Generate the sine series
sine_series = np.sin(frequency * time)

# Plot the sine series
plt.plot(time, sine_series)
plt.title('Sine Series')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
