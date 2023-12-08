def main():
    str1 = str(input("Input: ")).lower.strip()
    print(value(str1))

def value(greeting):
    options = ["hello", "HELLO"]

    if greeting in options:
        return 0
    elif "h" == greeting[0] and options != greeting:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
