def main():
    meow(get_number("how much meow do you want?"))

def get_number(prompt):
    while True:
        n = int(input(prompt))
        if n > 0:
            return n

def meow(n):
    for i in range(n):
        print("neow")


main()


