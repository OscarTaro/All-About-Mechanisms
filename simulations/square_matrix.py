import numpy as np
import matplotlib.pyplot as plt

unit_square = np.array([
    [0,0],
    [1,0],
    [1,1],
    [0,1],
    [0,0]
])

x = unit_square[:,0]
y = unit_square[:,1]

plt.figure(figsize=(4,4))
plt.plot(x, y, linewidth=2)
plt.fill(x, y , color="skyblue", alpha=0.5)
plt.title("Example 3.6: The Unit Square")
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.margins(0.5)
plt.axis("equal")
plt.grid(True)
plt.show()