#Crank and slider position analysis
# 04/04/2026
# Oscar T Mhlanga

import numpy as np
import matplotlib.pyplot as plt


# constants (m)
a, d, p, N = 0.100, 0.150, 0.300, 361

# 1D Arrays
theta2 = np.linspace(0, 2*np.pi, N)
theta3 = np.arctan2(-a*np.sin(theta2), (d - a*np.cos(theta2)))

# For reusing unit vectors
def unit_vector(t, t_2):
    e_2x, e_2y = np.cos(theta2), np.sin(theta2)
    e_3x, e_3y = np.cos(theta3), np.sin(theta3)
    return e_2x, e_2y, e_3x, e_3y
    
e_2x, e_2y, e_3x, e_3y = unit_vector(theta2, theta3)

B_x = a*e_2x
B_y = a*e_2y

P_x = B_x + p*e_3x
P_y = B_y+ p*e_3y

fig, ax = plt.subplots(figsize=(8,8))

ax.plot(B_x, B_y, 'g--', lw = 1, label="Path of B")
ax.plot(P_x, P_y, 'r-', lw = 1, label="Path of P")

i = 80
ax.plot([0, B_x[i]], [0, B_y[i]], 'k-', lw=3)
ax.plot([B_x[i], P_x[i]], [B_y[i], P_y[i]], 'k-', lw=3)

ax.text(0.01, 0, 'A' )
ax.text(B_x[i]+ 0.01, B_y[i], 'B' )
ax.text(d, 0.01, 'D', )
ax.text(P_x[i]+0.01, P_y[i], 'P' )

ax.plot([0, B_x[i], d, P_x[i]], [0, B_y[i], 0, P_y[i]], 'bo', label="Joints")

ax.legend()
ax.set_title("Three-Bar Linkage Position Analysis")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_aspect("equal")

plt.grid(True, linestyle='--')
plt.show()