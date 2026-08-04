import matplotlib.pyplot as plt
import numpy as np

shape = input("Enter shape (rectangle/triangle/circle): ").lower()

if shape == "rectangle":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    x = [x1, x2, x2, x1, x1]
    y = [y1, y1, y2, y2, y1]

    plt.plot(x, y, color='blue')
    plt.fill(x, y, color='lightblue', alpha=0.7)

elif shape == "triangle":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))

    x = [x1, x2, x3, x1]
    y = [y1, y2, y3, y1]

    plt.plot(x, y, color='green')
    plt.fill(x, y, color='lightgreen', alpha=0.7)

elif shape == "circle":
    r = float(input("Enter radius: "))
    theta = np.linspace(0, 2 * np.pi, 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.plot(x, y, color='red')
    plt.fill(x, y, color='pink', alpha=0.5)

else:
    print("Invalid shape")
    raise SystemExit

plt.title('User-Defined 2D Shape')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.grid(True)
plt.show()