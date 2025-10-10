import sys

while True:
    try:
        print("hello ,my name is",sys.argv[1])
        break
    except IndexError:
        continue
