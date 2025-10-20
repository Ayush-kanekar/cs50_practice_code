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
        for que in range(10):
            x = random.randint(0,9)
            y = random.randint(0,9)
            while True:
                z = y + x
                try:
                    if tries == 3:
                        print(f"{x} + {y} = {z}")
                        print('que',que)
                        que += 1
                        tries = 0
                        print('que',que)
                        break
                    ans = int(input(f"{x} + {y} = "))
                    if ans == z:
                        correct = correct + 1
                        que += 1
                        tries= 0
                        print("tries",tries)
                        break
                    else:
                        tries += 1
                        print('tries',tries)
                        print("EEE")
                        continue
                except ValueError:
                    tries += 1
    print("que",que)

def get_int(x,y):
    #To take input from the user about the answer
    tr = 0
    while True:
        try:
            if tr == 3:
                break
            answer 
            return answer
        except ValueError:
            tr += 1
            pass



if __name__ == "__main__":
    main()
