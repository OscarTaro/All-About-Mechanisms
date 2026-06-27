#"Example 3.7: Projectile Squares"
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt

square = np.array([
    [0, 0], 
    [5, 0], 
    [5, 5], 
    [0, 5], 
    [0, 0]
])

num_s = 20

t = np.linspace(0, 10, num_s, endpoint=False)
colors = cm.rainbow(np.linspace(0, 1, num_s))

#constants
v_x = 10 
v_y = 40 
g = 9.81

plt.figure(figsize=(8, 6))

for i in range(num_s):
    # Physics Equations (Kinematics)
    x = v_x * t[i]
    y = v_y * t[i] - 0.5 * g * (t[i]**2)

    # Transform the Square
    new_square = square + [x, y]

    # Plot
    plt.fill(new_square[:, 0], new_square[:, 1], 
             color=colors[i], alpha=0.6, edgecolor='black')

plt.title("Projectile Motion of Squares")
plt.xlabel("Distance (x)")
plt.ylabel("Height (y)")
plt.axis("equal")
plt.grid(True, linestyle="--")
plt.show()