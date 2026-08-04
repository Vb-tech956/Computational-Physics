import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

print("Choose condition:")
print("1. Falling object WITHOUT air resistance")
print("2. Falling object WITH air resistance")
choice = input("Enter 1 or 2: ")

m = int(input("Enter mass of the object falling: "))      
g = 9.8       

if choice == "1":
    c = 0.0   
    print("\nSimulating free fall (no air resistance)...")
else:
    c = float(input("Enter drag coefficient (e.g., 0.5): "))
    print(f"\nSimulating fall with air resistance (c = {c})...")

def falling_object(t, y):
    pos, vel = y
    dydt = [vel, -g - (c/m)*vel]
    return dydt

y0 = [0.0, 0.0]  

t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 200)

sol = solve_ivp(falling_object, t_span, y0, t_eval=t_eval)

t = sol.t
pos = sol.y[0]
vel = sol.y[1]

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(t, pos, label="Position")
plt.title("Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid()

plt.subplot(1,2,2)
plt.plot(t, vel, label="Velocity", color="orange")
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid()

plt.tight_layout()
plt.show()
