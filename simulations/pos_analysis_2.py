# Position Analysis of the Slider-Crank Using MATLAB®
# 08/04/2026
# Oscar T Mhlanga

import numpy as np
import matplotlib.pyplot as plt


# constants (m)
a, b, N = 40, 120, 100

# 1D Arrays
theta2 = np.linspace(0, 2*np.pi, N)
theta3 = np.arcsin(-a*np.sin(theta2)/b)

# Position Calculations
B_x = a*np.cos(theta2)
B_y = a*np.sin(theta2)

C_x = B_x + b*np.cos(theta3)
C_y = B_y + b*np.sin(theta3)

# Plots of Positions on Path B and P
plt.ion()
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(B_x, B_y, 'g--', lw = 1, label="Path of B")
ax.plot(C_x, C_y, 'r--', lw = 1, label="Path of P")

# Dynamic Plots
links, = ax.plot([], [], 'k-', lw=3) 
joints, = ax.plot([], [], 'bo') 

for i in range(N):
    # Remove ghost windows
    if not plt.fignum_exists(fig.number):
        break

    # Plots of Linkages
    links.set_data([0, B_x[i], C_x[i]], [0, B_y[i], C_y[i]]) 

    #Plots of Joints
    joints.set_data([0, B_x[i], C_x[i]], [0, B_y[i], C_y[i]]) 

    # Format Data
    ax.set_title(f"Position Analysis of the Slider-Crank Using MATLAB®")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_aspect("equal")
    ax.legend()
    ax.grid(True, linestyle='--') 

    # Show the Human
    plt.pause(0.06)

# Text labels
ax.text(0.1, 0.1, 'A' )
ax.text(B_x[i]+ 0.1, B_y[i]+0.1, 'B' )
ax.text(C_x[i]+0.1, C_y[i]+ 0.1, 'C' )

plt.ioff()
plt.show()