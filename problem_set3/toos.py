import random
import matplotlib.pyplot as plt

heads = 0
tails = 0
ratios = []
trials = 10000

for i in range(1, trials + 1):
    if random.choice(["head", "tails"]) == "head":
        heads += 1
    else:
        tails += 1
    ratios.append(heads / i * 100)

plt.plot(ratios)
plt.axhline(50, color="red", linestyle="--")
plt.xlabel("Number of flips")
plt.ylabel("Percentage of heads")
plt.title("Coin Flip Simulation")
plt.show()

