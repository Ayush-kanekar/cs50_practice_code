str_x,str_y,str_z = (input("Expression: ")).split()
x = int(str_x)
y = str_y
z = int(str_z)

if y == "+":
    print(f"{x + z :.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
    print(f"{x / z:.1f}")
