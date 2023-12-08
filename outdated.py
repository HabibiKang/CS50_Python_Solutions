months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").title()
        if "/" in date:
            convert = date.strip()
            new = convert.split("/") # input: month - day - year
            if len(new[2]) < 4:
                continue
            elif len(new[2]) > 4:
                continue
            elif len(new[2]) == 4:
                year = new[2]
                day = new[1]
                month = new[0]
                if int(month) > 12:
                    continue
                elif int(day) > 31:
                    continue
                elif len(month) == 1 and len(day) == 2:
                    print(f"{year}-0{month}-{day}")
                    break
                elif len(month) == 2 and len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(month) == 1 and len(day) == 1:
                    print(f"{year}-0{month}-0{day}")
                    break
                elif len(month) == 2 and len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break


        elif "," in date:
            new1 = date.replace(",", "")
            new2 = str(new1).strip()
            new3 = new2.split(" ")

            if new3[0] == "January":
                day = new3[1]
                year = new3[2]
                month = "01"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "February":
                day = new3[1]
                year = new3[2]
                month = "02"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "March":
                day = new3[1]
                year = new3[2]
                month = "03"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "April":
                day = new3[1]
                year = new3[2]
                month = "04"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "May":
                day = new3[1]
                year = new3[2]
                month = "05"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "June":
                day = new3[1]
                year = new3[2]
                month = "06"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "July":
                day = new3[1]
                year = new3[2]
                month = "07"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "August":
                day = new3[1]
                year = new3[2]
                month = "08"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "September":
                day = new3[1]
                year = new3[2]
                month = "09"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "October":
                day = new3[1]
                year = new3[2]
                month = "10"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "November":
                day = new3[1]
                year = new3[2]
                month = "11"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break
            elif new3[0] == "December":
                day = new3[1]
                year = new3[2]
                month = "12"
                if int(day) > 31:
                    continue
                elif len(year) != 4:
                    continue
                elif len(day) == 1:
                    print(f"{year}-{month}-0{day}")
                    break
                elif len(day) == 2:
                    print(f"{year}-{month}-{day}")
                    break

    except ValueError:
        continue
