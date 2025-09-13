grocery = {}
while True:
    try :
        item = input().upper()
    except EOFError:
        print()
        break
    count = grocery.setdefault(item,0)
    grocery[item] = count +1

for item ,count in sorted(grocery.items()):
    print(count, item)
