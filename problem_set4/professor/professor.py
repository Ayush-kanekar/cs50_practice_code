import random


def main():
    level = get_level()
    num = generate_integer(level)

def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x in (1,2,3):
                return x
        except ValueError:
            pass

def generate_integer(lev):
    que = 0
    correct = 0
    tries = 0
    if lev == 1:
        for que in range(11):
            x = random.randint(0,9)
            y = random.randint(0,9)
            z = y + x
            ans = get_int(x,y)
            if ans == z:
                correct = correct + 1
                tries= 0
            elif tries == 3:
                print(f"{x} + {y} = {z}")
                que += 1
            else:
                print("EEE")
                continue


def get_int(x,y):
    tr = 0
    while True:
        try:
            if tr == 3:
                break
            answer = int(input(f"{x} + {y} = "))
            return answer
        except ValueError:
            tr += 1
            pass



if __name__ == "__main__":
    main()
