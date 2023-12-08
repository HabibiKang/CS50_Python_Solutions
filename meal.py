def main():
    time = input("What time is it? ")
    ans = convert(time)

    if ans >= 7 and ans <= 8:
        print("breakfast time")
    elif ans >= 12 and ans <= 13:
        print("lunch time")
    elif ans >= 18 and ans <= 19:
        print("dinner time")

def convert(time):
    new_time = time.split(":")
    mins = float(new_time[1])
    new_mins = int(mins) / 60
    return float(new_time[0]) + new_mins



if __name__ == "__main__":
    main()


# implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
# If it’s not time for a meal, don’t output anything at all.
#
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal’s time range is inclusive.
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
