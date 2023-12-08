import re
import sys

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))

def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        valids = ip.split(".")
        for num in valids:
            if int(num[0]) < 0 or int(num[0]) > 255:
                return False
            elif int(num) < 0 or int(num) > 255:
                return False

        return True
    else:
        return False


if __name__ == "__main__":
    main()
