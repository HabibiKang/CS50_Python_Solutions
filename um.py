import re
import sys


def main():
    text = input("Text: ")
    print(count(text))



def count(text):
    pattern = r"\bum\b"
    ans = re.findall(pattern, text, re.IGNORECASE)
    return len(ans)


if __name__ == "__main__":
    main()
