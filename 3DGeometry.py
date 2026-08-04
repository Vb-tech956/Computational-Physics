import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

shape = input("Enter shape (cube/sphere/pyramid): ").lower()

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

if shape == "cube":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    z1 = float(input("Enter z1: "))
    size = float(input("Enter size: "))

    points = [
        [x1, y1, z1],
        [x1 + size, y1, z1],
        [x1 + size, y1 + size, z1],
        [x1, y1 + size, z1],
        [x1, y1, z1 + size],
        [x1 + size, y1, z1 + size],
        [x1 + size, y1 + size, z1 + size],
        [x1, y1 + size, z1 + size],
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    for i, j in edges:
        x = [points[i][0], points[j][0]]
        y = [points[i][1], points[j][1]]
        z = [points[i][2], points[j][2]]
        ax.plot(x, y, z, color='blue')

elif shape == "sphere":
    r = float(input("Enter radius: "))
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.7)

elif shape == "pyramid":
    x1 = float(input("Enter base x1: "))
    y1 = float(input("Enter base y1: "))
    x2 = float(input("Enter base x2: "))
    y2 = float(input("Enter base y2: "))
    height = float(input("Enter height: "))

    base = [(x1, y1, 0), (x2, y1, 0), (x2, y2, 0), (x1, y2, 0)]
    apex = [(x1 + (x2 - x1) / 2), (y1 + (y2 - y1) / 2), height]

    for p in base:
        ax.plot([p[0], apex[0]], [p[1], apex[1]], [p[2], apex[2]], color='green')

    for i in range(len(base)):
        p1 = base[i]
        p2 = base[(i + 1) % len(base)]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='green')

else:
    print("Invalid shape")
    raise SystemExit

ax.set_title('User-Defined 3D Shape')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.show()