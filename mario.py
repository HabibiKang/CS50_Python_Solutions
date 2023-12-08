def main():
    while True:
        try:
            height = int(input("Height: "))
            if height < 1:
                continue
            elif height not in range(1, 9):
                continue
            else:
                for i in range(1, height + 1):
                    spaces = " " * (height - i)
                    hashes = "#" * i
                    print(f"{spaces}{hashes}")
                break
        except ValueError:
            continue


if __name__ == "__main__":
    main()
