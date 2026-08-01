num_ac = int(input("Enter number of AC's:"))
resistance_per_ac = int(input("Enter resistance of each AC (ohms):"))
supply_voltage = int(input("Enter total voltage supply (volts):"))

total_resistance = num_ac * resistance_per_ac
current = supply_voltage / total_resistance

print("\nSeries Load Simulation")
print(f"Number of ACs : {num_ac}")
print(f"Total resistance : {total_resistance:.2f} Ohms")
print(f"Circuit current : {current:.2f} Amphere/n")

for i in range(1, num_ac + 1):
    voltage = current * resistance_per_ac
    power = voltage * current
    print(f"AC {i} : Voltage = {voltage:.2f}V, Current = {current:.2f}A, Power = {power:.2f}W")