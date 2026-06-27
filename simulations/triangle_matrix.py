import numpy as np
import matplotlib.pyplot as plt

triangle = np.array([
    [0,0],
    [1,0],
    [0.5,np.sqrt(3/2)],
    [0,0]
])

x = triangle[:, 0]
y = triangle[:, 1]

plt.figure(figsize=(4,4))
plt.plot(x, y, color="black", linewidth=2)
plt.fill(x, y, color='skyblue', alpha=0.5)
plt.title("Unit Triangle ")
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.grid(True)
plt.show()