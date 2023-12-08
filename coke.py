# implement a program that prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due.
# Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

amount_due = 50

while True:

    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert coin: "))
    if coin not in[25, 10, 5]:
        continue

    elif amount_due > 0 and coin < amount_due:
        amount_due -= coin

    elif amount_due > 0 and coin == amount_due:
        print(f"Change Owed: 0")
        break

    elif coin > amount_due:
        change = int(coin) - int(amount_due)
        print(f"Change Owed: {change}")
        break

    elif amount_due == 0:
        print(f"Change Owed: 0")
        break


