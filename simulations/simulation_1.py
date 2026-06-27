import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt

square = np.array([
    [0,0],
    [1,0],
    [1,1],
    [0,1],
    [0,0]
])

plt.figure(figsize=(4,4))
num_squares = 12
t = np.linspace(0, 2*np.pi, num_squares, endpoint=False)
r = 2
colors = cm.rainbow(np.linspace(0, 1, num_squares))

for i in range(num_squares):
    r_x = r*np.cos(t[i]) 
    r_y = r*np.sin(t[i])
    

    new_square = square + [r_x, r_y]
    plt.fill(new_square[:,0], new_square[:,1], color=colors[i], alpha = 0.5)

plt.title("Example 3.7: Squares Rotating in a Circle")
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.axis("equal")
plt.margins(0.5)
plt.grid(True, linestyle=":")
plt.show()