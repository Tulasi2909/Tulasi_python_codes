x = int(input("enter first number: "))
y = int(input("enter second number: "))
mathematical_operations = input("enter mathematical operator: ")
if mathematical_operations == "+":
    sum = x+y
    print(f"answer= {sum}")
elif mathematical_operations == "-":
    diff = x-y
    print(f"answer= {diff}")
elif mathematical_operations == "/":
    div = x/y
    print(f"answer= {div}")
elif mathematical_operations == "*":
    mul = x*y
    print(f"answer= {mul}")
else:
    print("not a valid mathematical operator")









