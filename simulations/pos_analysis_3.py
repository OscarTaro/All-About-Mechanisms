# Finding the Position of Any Point on the Linkage
# 16/04/2026
# Oscar T Mhlanga

import numpy as np
import matplotlib.pyplot as plt

# Constants (cm) and (radians)
a, b, c, d, p = 2, 3.2, 3, 1.5, 2
alpha = np.radians(20)
theta2 = np.radians(30)

# parameters for delta
r = d - a*np.cos(theta2)
s = a*np.sin(theta2)
f = np.sqrt(r**2 + s**2)

arg = (b**2 + c**2 - f**2) / (2 * b * c)
# Check Grashoff Condition
if not (-1<= arg <=1):
    print('Checking Grashoff Condition')
    if not (d + b < a + c):
        print('Non-Grashoff Fourbar Linkage')
    elif not (d + b == a + c):
        print('Special Case Fourbar Linkage')

else:

    delta = np.arccos(arg)

    g = b - c*np.cos(delta)
    h = c*np.sin(delta)

    # Calculation for theta3
    theta3 = np.arctan2(h*r - s*g, g*r + s*h)

    # Calculations for Positions B, C and P
    B_x = a*np.cos(theta2)
    B_y = a*np.sin(theta2)

    C_x = B_x + b*np.cos(theta3)
    C_y = B_y + b*np.sin(theta3)

    P_x = B_x + p*np.cos(alpha + theta3)
    P_y = B_y + p*np.sin(alpha + theta3)

    # Subplots for multiple parts, its best practise
    fig, ax = plt.subplots(figsize=(10,6))

    # Plots for Linkages
    ax.plot([0, B_x], [0, B_y], 'k-', lw=2, label='Crank')
    ax.plot([B_x, P_x, C_x], [B_y, P_y, C_y], lw=2, label='Coupler')
    ax.fill([B_x, P_x, C_x], [B_y, P_y, C_y], color='skyblue')
    ax.plot([d, C_x], [0, C_y], 'k-', lw=2, label='Rocker')
    ax.plot([0, B_x, C_x, d], [0, B_y, C_y, 0], 'ko', label='Joints')

    # Joint Labels
    ax.text(0, 0, 'A', ha='right')
    ax.text(B_x, B_y, 'B', ha='center')
    ax.text(P_x, P_y, 'P')
    ax.text(C_x, C_y, 'C')
    ax.text(d, 0, 'D')

    # Format Data
    ax.set_title('Finding the Position of Any Point on the Linkage')
    ax.set_xlabel('x-positions (cm)')
    ax.set_ylabel('y-positions (cm)')
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(-0.5, 5)
    plt.legend()
    plt.grid(True)
    plt.show()