camal_case = str(input("camelCase: "))
print("snake_case: ",end="")
for c in camal_case:
    if c .isupper():
        print("_" + c.lower(),end="")
    elif c == "%":
        continue
    else: 
        print(c, end="")

