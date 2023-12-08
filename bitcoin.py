import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(get_price(n))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

def get_price(n):
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        price = r.json()
        price2 = price["bpi"]["USD"]["rate_float"]
        ans = price2 * n
        return f"${ans:,.4f}"
    except requests.RequestException:
        return None

if __name__ == "__main__":
    main()
