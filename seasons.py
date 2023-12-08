from datetime import date
import inflect
import sys

def main():
    try:
        y, m, d = str(input("DOB: ")).split("-")
        print(get_mins(y,m,d))
    except ValueError:
        sys.exit("Invalid date")


go = inflect.engine()

def get_mins(y, m, d):
    try:
        day = date(int(y), int(m), int(d))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    ans = today - day
    mins = int(ans.total_seconds() / 60)
    new_ans = go.number_to_words(mins, andword="")
    return f"{new_ans.capitalize()} minutes"

if __name__ == "__main__":
    main()
