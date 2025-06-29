import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y, label='sin(x)', color='blue', linestyle='--', linewidth=2)
plt.title("📈 Line Chart: Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()