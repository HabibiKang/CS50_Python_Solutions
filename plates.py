import re
def main():
    plate = input("Plate: ").lower()
    if is_valid(plate) == True:
        print("Valid")
    elif is_valid(plate) == False:
        print("Invalid")

def is_valid(plate):
    if re.search(r"[^A-Za-z0-9]", plate):
        return False

    elif len(plate) == 5 and plate.isalpha() == True:
        return True
    elif len(plate) == 6 and plate.isalpha() == True:
        return True

    elif len(plate) == 6 and plate[-1][0].isdigit() == True:
        middle = plate[len(plate)//2]
        if middle.isdigit() == False and middle != "0":
            return True

    elif len(plate) == 6:
        return True

    elif len(plate) > 6 or len(plate) < 2:
        return False

    elif plate[0].isalpha() == False and plate[1].isalpha() == False:
        return False

    elif len(plate) == 3 or len(plate) == 4 or len(plate) == 5:
        middle = plate[len(plate)//2]
        if middle.isdigit() and middle != "0":
            if plate[0] != 0:
                return True
            else:
                return False

        else:
            return False
    else:
        if plate[0] == "0":
            return False
        elif len(plate) == 5:
            if plate[0].isalpha() == False or plate[-1].isalpha() == False:
                return False
            return True

if __name__ == "__main__":
  main()
