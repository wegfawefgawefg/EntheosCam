
from matplotlib import pyplot as plt
import numpy as np

start = 10
end = 0

duration = 100
x = np.linspace(-10, 10, 8)
positions = 1/(1 + 1.5**-x)
positions = positions * (end - start) + start
plt.plot(positions)
plt.show()

# deltas = np.diff(positions)
# plt.plot(deltas)
# plt.show()

