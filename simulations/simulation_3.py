import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt

square = np.array([
    [-2.5, -2.5], 
    [ 2.5, -2.5], 
    [ 2.5,  2.5], 
    [-2.5,  2.5], 
    [-2.5, -2.5]
])

num_s = 20

t = np.linspace(0, 10, num_s, endpoint=False)
colors = cm.rainbow(np.linspace(0, 1, num_s))


v_x = 10 
v_y = 40 
g = 9.81
w = 2

plt.ion()
fig, ax = plt.subplots(figsize=(8, 6))

for i in range(num_s):
    
    x = v_x * t[i]
    y = v_y * t[i] - 0.5 * g * (t[i]**2)
    theta = w*t[i]
    r = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    rotated_square = square @ r
    final_square = rotated_square + [x, y]

    ax.cla()
    ax.fill(final_square[:, 0], final_square[:, 1], 
             color=colors[i], alpha=0.6, edgecolor='black')
    ax.set_xlim(-50, 150)
    ax.set_ylim(-100, 150)
    ax.grid(True, linestyle="--")
    ax.set_title("Primitive Animation")
    ax.set_xlabel("distance (mm)")
    ax.set_ylabel("height (mm)")
    plt.pause(0.06)

plt.ioff()
plt.show()