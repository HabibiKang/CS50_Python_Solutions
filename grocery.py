items = {}
while True:
    try:
        item = input().upper()
        items[item] = items.get(item, 0)+1
    except EOFError:
           break

for item, items in sorted(items.items()):
     print(f"{items} {item}")
