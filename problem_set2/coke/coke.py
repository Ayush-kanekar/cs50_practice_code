accepted_coins = [5,10,25]
amount = 50
while amount >0 :
    insert_coin = int(input("Insert coin: "))
    if insert_coin in accepted_coins:
        amount = amount - insert_coin
    else:
        print(f"Amount Due: {amount}\n")
        continue
    if amount <= 0:
        print(f"Charged Owed: {abs(amount)}")
