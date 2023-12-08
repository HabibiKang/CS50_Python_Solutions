
def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percent = convert(fraction)
            print(gauge(percent))
        except ValueError:
            print("ValueError")

def convert(fraction):
    try:
        new = fraction.split("/")
        x = int(new[0])
        y = int(new[1])
        return round((int(x)/int(y)) * 100)
    except (ValueError, ZeroDivisionError) as e:
        raise e

def gauge(math2):
    math2 = str(math2)
    new_m1 = float(math2)
    new_m2 = int(new_m1)
    new_m3 = round(new_m2, 0)
    new_m4 = str(new_m3)
    final = new_m4.split(".")
    answer = int(final[0])
    ans = f"{answer}%"
    if ans == "1%" or ans == "0%":
        return("E")
    elif ans == "99%" or ans == "100%":
        return("F")
    else:
        return(ans)

if __name__ == "__main__":
    main()
