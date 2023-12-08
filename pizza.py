from csv import reader, DictReader
from tabulate import tabulate
import sys

def main():
    if sys.argv[1] == "regular.csv" and len(sys.argv[1]) == 11:
        regular()
    elif sys.argv[1] == "sicilian.csv" and len(sys.argv[1]) == 12:
        sicilian()
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[-1] != "v":
        sys.exit("Not a CSV file")
    else:
        print("File does not exist")


def regular():
     with open("regular.csv", "r") as file:
        reader1 = reader(file)
        table = tabulate(reader1, headers = "firstrow", tablefmt="grid")
        print(table)

def sicilian():
    with open("sicilian.csv", "r") as file:
        reader1 = reader(file)
        table = tabulate(reader1, headers = "firstrow", tablefmt="grid")
        print(table)


if __name__ == "__main__":
    main()
