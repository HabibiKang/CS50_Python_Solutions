import re
import sys


def main():
    embed = input("HTML: ").strip()
    print(parse(embed))

url1 = "http://youtube.com/embed/xvFZjo5PgG0"
url2 = "http://www.youtube.com/embed/xvFZjo5PgG0"
url3 = "https://youtube.com/embed/xvFZjo5PgG0"
url4 = "https://www.youtube.com/embed/xvFZjo5PgG0"

def parse(embed):
    if "<iframe" not in embed or "src=" not in embed:
        return None

    elif url1 in embed:
        new1 = url1.replace(".com", "")
        new2 = str(new1).replace("embed/", "")
        new3 = str(new2).replace("ube", "u.be")
        new4 = str(new3).replace("tp:", "tps:")
        return new4

    elif url2 in embed:
        new1 = url2.replace(".com", "")
        new2 = str(new1).replace("embed/", "")
        new3 = str(new2).replace("ube", "u.be")
        new4 = str(new3).replace("tp:", "tps:")
        new5 = str(new4).replace("www.", "")
        return new5


    elif url3 in embed:
        new1 = url3.replace(".com", "")
        new2 = str(new1).replace("embed/", "")
        new3 = str(new2).replace("ube", "u.be")
        return new3

    elif url4 in embed:
        new1 = url4.replace(".com", "")
        new2 = str(new1).replace("embed/", "")
        new3 = str(new2).replace("ube", "u.be")
        new4 = str(new3).replace("www.", "")
        return new4

    else:
        return None

if __name__ == "__main__":
    main()
