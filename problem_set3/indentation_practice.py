def greet(name):
    print("Hello, " + name)
    if len(name) > 3:
    print("That's a pretty long name")
    else:
    print("Short and sweet!")

for i in range(5):
print(i)
if i % 2 == 0:
print("even")
else:
print("odd")

while True:
answer = input("Say something (q to quit): ")
if answer == "q":
break
else:
print("You said:", answer)

