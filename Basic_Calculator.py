a = int(input("Enter first number:"))
op = input("Enter operator ('+','-','*','/'):")
b = int(input("Enter second number:"))
 
if op == "+":
    print("Result:",a+b)
elif op =="-":
    print("Result:",a-b)
elif op == "*":
    print("Result:",a*b)
elif op =="/":
    if b != 0:
        print("Result:",a/b)
    else:
        print("Error! Division by zero is not possible")
else:
    print("Invalid operator!")