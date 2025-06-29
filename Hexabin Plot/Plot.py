import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10000)
y = np.random.rand(10000)

plt.hexbin(x, y, gridsize=50, cmap='Blues', mincnt=1)
plt.colorbar(label='Counts')
plt.title('Hexabin Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()