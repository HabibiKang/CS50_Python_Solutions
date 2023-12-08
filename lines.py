import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


    elif len(sys.argv) == 2 and ".py" not in sys.argv[1]:
            sys.exit("Not a Python file")
    else:
        print(count(sys.argv[1]))

def count(file):
    try:
        ans = 0
        with open(file, "r") as file:
            for line in file:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                   ans += 1
            return ans

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
