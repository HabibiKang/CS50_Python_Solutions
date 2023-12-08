import re

def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    elif is_valid(plate) == False:
        print("Invalid")

def is_valid(plate):
    if len(plate) == 6 and plate.isalpha():
        return True
    elif len(plate) == 6 and plate[-1].isdigit() and plate[-2].isalpha():
        return False
    elif re.search(r"[^A-Za-z0-9]", plate):
        return False
    elif len(plate) == 4:
        if plate[0].isalpha() == True and plate[1].isalpha() == True:
            if plate[2] == "0":
                return False
            else:
                return True

    elif len(plate) == 6 and plate[-1][0].isdigit() == True:
        middle = plate[len(plate)//2]
        if middle.isdigit() == False or middle != "0":
            if plate[-1].isalpha() and plate[-2].isdigit():
                return False
            else:
                return True
        elif len(plate) == 5 and middle.isdigit() == True:
            return False
        elif plate[2].isdigit() == False:
            return False
    elif len(plate) == 5 and plate[-1] == "P":
        return False

    elif plate[-1].isdigit() and plate[-2].isalpha():
        return False

    elif len(plate) > 6 or len(plate) < 2:
        return False

    elif plate[0].isalpha() == False and plate[1].isalpha() == False:
        return False

    elif len(plate) == 3 or len(plate) == 4 or len(plate) == 5:
        middle = plate[len(plate)//2]
        if middle.isdigit() == True:
            return False

        else:
            return False

    elif plate[0] == "0":
        return False
    elif len(plate) == 5:
        if plate[0].isalpha() == False or plate[-1].isalpha() == False:
            return False

if __name__ == "__main__":
    main()
