import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y =  generate_integer(level)
        tries = 0
        while tries < 3:
            try:
                print(f"{x} + {y} = ",end="")
                ans = int(input())
                if ans == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        if tries == 3:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
        if level == 1:
            start,end = 0,9
        elif level == 2:
            start,end = 10,99
        else:
            start, end = 100,999
        return random.randint(start, end)
if __name__ == "__main__":
    main()
