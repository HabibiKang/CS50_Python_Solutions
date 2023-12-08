names = {}

while True:
    try:
        name = input("Name: ").capitalize().strip()
        names[name] = names.get(name, 0) + 1
        new_names = list(names.keys())

    except EOFError:
        if len(new_names) == 1:
            print(f"Adieu, adieu, to {new_names[0]}")
        elif len(new_names) == 2:
            print(f"Adieu, adieu, to {new_names[0]} and {new_names[1]}")
        elif len(new_names) == 3:
            print(f"Adieu, adieu, to {new_names[0]}, {new_names[1]}, and {new_names[2]}")
        elif len(new_names) == 4:
            print(f"Adieu, adieu, to {new_names[0]}, {new_names[1]}, {new_names[2]}, and {new_names[3]}")
        elif len(new_names) == 5:
            print(f"Adieu, adieu, to {new_names[0]}, {new_names[1]}, {new_names[2]}, {new_names[3]}, and {new_names[4]}")
        elif len(new_names) == 6:
            print(f"Adieu, adieu, to {new_names[0]}, {new_names[1]}, {new_names[2]}, {new_names[3]}, {new_names[4]}, and {new_names[5]}")
        elif len(new_names) == 7:
            print(f"Adieu, adieu, to {new_names[0]}, {new_names[1]}, {new_names[2]}, {new_names[3]}, {new_names[4]}, {new_names[5]}, and {new_names[6]}")
        elif len(new_names) == 8:
            print(f"Adieu, adieu, to {new_names[0]}, {new_names[1]}, {new_names[2]}, {new_names[3]}, {new_names[4]}, {new_names[5]}, {new_names[6]}, and {new_names[7]}")

        break

