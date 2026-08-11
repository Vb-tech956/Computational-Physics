# 1. Arithmetic operators

# 2. Relational operators
a, b = 10, 20
print(a > b)   # False
print(a <= b)  # True

# 3. Logical operators
x, y = True, False
print(x and y) # False
print(x or y)  # True
print(not x)   # False

# 4. Assignment operators
num = 5
num += 3       # num = num + 3
print(num)     # 8

# 5. Bitwise operators
p, q = 6, 3    # binary: 110 and 011
print(p & q)   # AND → 2
print(p | q)   # OR  → 7
print(p ^ q)   # XOR → 5
print(~p)      # NOT → -7
print(p << 1)  # Left shift → 12
print(p >> 1)  # Right shift → 3

# 6. Membership operators
mylist = [1, 2, 3]
print(2 in mylist)     # True
print(5 not in mylist) # True

# 7. Identity operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)      # True (same object)
print(x is z)      # False (different objects)
print(x is not z)  # True
