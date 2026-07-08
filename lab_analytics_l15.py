import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

time = np.array([0, 2, 4, 6, 8, 10, 12, 14])
pH = np.array([7.0, 6.5, 5.8, 4.2, 3.5, 2.9, 2.3, 2.1])

slope, intercept, r_value, p_value, std_err = stats.linregress(time, pH)

fig, ax = plt.subplots()

ax.errorbar(time, pH, yerr=std_err, fmt='o', color='red', label='Measured pH')
ax.plot(time, slope * time + intercept, color='blue', label='Linear Fit')

ax.set_title("Automated Chemical Kinetics & pH Tracking")
ax.set_xlabel("Time (minutes)")
ax.set_ylabel("pH level")
ax.legend()
plt.show()