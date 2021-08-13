import matplotlib.pyplot as plt
import numpy as np

n = [105.0,    140.0,    150.0,    200.0,    500.0]
e = [0.808517, 0.814008, 0.814544, 0.810127, 0.792517]

plt.plot(n, e, linestyle='--', marker='o', color = (0.0, 0.0, 1.0) )
plt.grid(True)

plt.show()
