items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order = 0

# Get order from user
while True:
    try:
        item = str(input("Item: ")).title()
        for key in items:
            if item in items:
                ans = items[item]
                order += ans
                total = float(order)
                answer = str(total)
                print(f"Total: ${answer}0")
                break

            elif item not in items:
                continue

    except EOFError:
        break

    except KeyError:
        print("KeyError")
        continue

