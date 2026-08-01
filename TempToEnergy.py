k = 1.380649e-23
temperature = float(input("Enter temperature (K) : "))
energy = k * temperature
print(f"Temperature = {temperature}K")
print(f"Thermal Energy = {energy:.3e}J")