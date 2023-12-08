import csv
import sys


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    else:
        after(sys.argv[1], sys.argv[2])


def after(before, after):
    try:
        with open(before) as before:
            reader = csv.DictReader(before)
            with open(after, "w") as after:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(after, fieldnames = header)
                writer.writeheader()
                for students in reader:
                    last, first = students["name"].split(", ")
                    house = students["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("Could not read {before}")


if __name__ == "__main__":
    main()
