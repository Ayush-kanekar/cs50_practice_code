accepted_coins = [5,10,25]
amount = 50
while amount > 0 :
    print(f"Amount Due: {amount}")
    insert_coin = int(input("Insert coin: "))
    if insert_coin in accepted_coins:
        amount = amount - insert_coin
    else:
        continue

print(f":Change Owed: {abs(amount)}")
