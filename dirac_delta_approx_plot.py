import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.05)

for N in range(1,7):
	y = np.sin((N + 1 / 2) * np.pi * x) / (2 * np.sin(np.pi * x / 2))
	plt.plot(x, y)

plt.show()