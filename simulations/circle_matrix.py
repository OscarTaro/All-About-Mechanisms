import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
r = 1
x = r*np.cos(t)
y = r*np.sin(t)

circle_matrix = np.column_stack((x,y))

a = circle_matrix[:, 0]
b = circle_matrix[:, 1]

plt.figure(figsize=(4,4))
plt.plot(a, b, color="black", linewidth=2)
plt.fill(a, b, color="skyblue", alpha=0.5)
plt.title("Parametric unit Circle")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axis("equal")
plt.margins(0.2)
plt.grid(True, linestyle="--")
plt.show()