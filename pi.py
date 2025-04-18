import numpy as np
import matplotlib.pyplot as plt
radius = 1
num_points =50
theta = np.linspace(0, 2 * np.pi, num_points)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
fig, ax = plt.subplots()
ax.scatter(x,y, color='black', s=50)
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-1.2,1.2)
ax.set_aspect('equal')
ax.set_axis_off()
plt.title("circle pattern plot")
plt.show()