<<<<<<< HEAD
import math
def find_roots(a,b,c):
    d = b**b - 4*a*c
    if d>a :
        root1 = (-b + math.sqrt(d)/2*a)
        root2 = (-b - math.sqrt(d)/2*a)
        return f"Two distinct real roots are :{root1},{root2}"
    elif d==0 :
        root = -b/(2*a)
    else :
        real_part = -b/(2*a)
        img_part = math.sqrt(-d)/(2*a)
        return f"Complex roots are : {real_part}+{img_part}i,{real_part}-{img_part}i"

print("Quadratic equation solver.")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

=======
import math
def find_roots(a,b,c):
    d = b**b - 4*a*c
    if d>a :
        root1 = (-b + math.sqrt(d)/2*a)
        root2 = (-b - math.sqrt(d)/2*a)
        return f"Two distinct real roots are :{root1},{root2}"
    elif d==0 :
        root = -b/(2*a)
    else :
        real_part = -b/(2*a)
        img_part = math.sqrt(-d)/(2*a)
        return f"Complex roots are : {real_part}+{img_part}i,{real_part}-{img_part}i"

print("Quadratic equation solver.")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

>>>>>>> f3b138de7eb0032475242e5d5ed6d17969df41d9
print(find_roots(a,b,c))