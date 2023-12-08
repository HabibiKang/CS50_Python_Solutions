import re
import sys

def main():
    hours = input("Hours: ").strip()
    print(convert(hours))

def convert(hours):
    if "AM" not in hours and "PM" not in hours:
        raise ValueError
    elif "to" not in hours:
        raise ValueError
    elif len(str(hours)) >= 21:
        raise ValueError
    elif len(str(hours)) <= 11:
        raise ValueError
    else:
        # IF FORMAT LOOKS LIKE 9 AM
        if re.search(r"^(\d+)\s(?:AM|PM)\sto\s(\d+)\s(?:AM|PM$)", hours):
            new_hrs1 = hours.split(" ")
            num1 = new_hrs1[0]
            if int(num1) > 12 or int(num1) <= 0:
                raise ValueError
            else:
                num1_am_pm = new_hrs1[1]
                to = new_hrs1[2]
                num2 = new_hrs1[3]
                if int(num2) > 12 or int(num2) <= 0:
                    raise ValueError
                else:
                    num2_am_pm = new_hrs1[4]

            # CONVERT NUM1 PM
            if num1_am_pm == "PM":
                if int(num1) >= 1 and int(num1) < 12:
                    new_num1 = int(num1) + 12
                    if len(str(new_num1)) == 2:
                        ans1 = f"{new_num1}:00"
                    elif len(str(new_num1)) == 1:
                        ans1 = f"0{new_num1}:00"
                else:
                    if len(str(num1)) == 2:
                        ans1 = f"{num1}:00"
                    elif len(str(num1)) == 1:
                        ans1 = f"0{num1}:00"

            # CONVERT NUM1 AM
            elif num1_am_pm == "AM":
                if int(num1) == 12:
                    ans1 = f"00:00"
                else:
                    if len(str(num1)) == 2:
                        ans1 = f"{num1}:00"
                    elif len(str(num1)) == 1:
                        ans1 = f"0{num1}:00"

            # CONVERT NUM2 PM
            if num2_am_pm == "PM":
                if int(num2) > 12 or int(num2) <= 0:
                    raise ValueError
                elif int(num2) >= 1 and int(num2) < 12:
                    new_num2 = int(num2) + 12
                    if len(str(new_num2)) == 2:
                        ans2 = f"{new_num2}:00"
                    elif len(str(new_num2)) == 1:
                        ans2 = f"0{new_num2}:00"
                else:
                    if len(str(num2)) == 2:
                        ans2 = f"{num2}:00"
                    elif len(str(num2)) == 1:
                        ans2 = f"0{num2}:00"

            # CONVERT NUM2 AM
            elif num2_am_pm == "AM":
                if int(num2) == 12:
                    ans2 = f"00:00"
                elif int(num2) == 11:
                    ans2 = f"11:00"
                elif int(num2) == 10:
                    ans2 = f"10:00"
                else:
                    if int(num2) > 12 or int(num2) <= 0:
                        raise ValueError
                    elif len(str(num2)) == 2:
                        ans2 = f"{num2}:00"
                    elif len(str(num2)) == 1:
                        ans2 = f"0{num2}:00"

            return f"{ans1} to {ans2}"

        elif re.search(r"^(\d+):(\d{2})\s(?:AM|PM)\sto\s(\d+):(\d{2})\s(?:AM|PM)$", hours):
            new_hrs2 = hours.split(" to ")
            time1 = new_hrs2[0]
            time2 = new_hrs2[1]
            new_time1 = time1.split(":")
            time1_hr = new_time1[0]
            if int(time1_hr) > 12 or int(time1_hr) <= 0:
                raise ValueError
            else:
                time1_mins = new_time1[1]
                new_time2 = time2.split(":")
                time2_hr = new_time2[0]
                if int(time1_hr) > 12 or int(time1_hr) <= 0:
                    raise ValueError
                else:
                    time2_mins = new_time2[1]
                    if int(time2_hr) > 12 or int(time2_hr) <= 0:
                        raise ValueError
                    else:
                        if "PM" in time1_mins:
                            time1_mins = str(time1_mins.strip(" PM"))
                            if int(time1_hr) == 12:
                                new_time1 = f"12:{time1_mins}"
                            elif int(time1_hr) == 11:
                                new_time1 = f"23:{time1_mins}"
                            elif int(time1_hr) == 10:
                                new_time1 = f"22:{time1_mins}"
                            new_time1_hr = int(time1_hr) + 12

                            if int(time1_mins) >= 60:
                                raise ValueError

                            elif len(str(new_time1_hr)) == 2:
                                new_time1 = f"{new_time1_hr}:{time1_mins}"
                            elif len(str(new_time1_hr)) == 1:
                                new_time1 = f"0{new_time1_hr}:{time1_mins}"
                            else:
                                raise ValueError

                        elif "AM" in time1_mins:
                            time1_mins = str(time1_mins.strip(" AM"))
                            if int(time1_hr) == 12:
                                new_time1 = f"00:{time1_mins}"
                            elif int(time1_hr) == 11:
                                new_time1 = f"23:{time1_mins}"
                            elif int(time1_hr) == 10:
                                new_time1 = f"22:{time1_mins}"
                            elif int(time1_mins) >= 60:
                                raise ValueError
                            elif time1_hr != 12:
                                time1_mins = str(time1_mins.strip(" AM"))
                                if int(time1_mins) >= 60:
                                    raise ValueError
                                elif len(str(time1_hr)) == 2:
                                    new_time1 = f"{time1_hr}:{time1_mins}"
                                elif len(str(time1_hr)) == 1:
                                    new_time1 = f"0{time1_hr}:{time1_mins}"

                    if "PM" in time2_mins:
                        if int(time2_hr) > 12 or int(time2_hr) <= 0:
                            raise ValueError
                        else:
                            new_time2_mins = time2_mins.strip(" PM")
                            if int(time2_hr) == 12:
                                new_time2 = f"12:{new_time2_mins}"
                            elif int(time2_hr) == 11:
                                new_time2 = f"23:{new_time2_mins}"
                            elif int(time2_hr) == 10:
                                new_time2 = f"22:{new_time2_mins}"

                            else:
                                new_time2_hr = int(time2_hr) + 12
                                if len(str(new_time2_hr)) == 2:
                                    new_time2 = f"{new_time2_hr}:{new_time2_mins}"
                                elif len(str(new_time2_hr)) == 1:
                                    new_time2 = f"0{new_time2_hr}:{new_time2_mins}"

                    elif "AM" in time2_mins:
                        if int(time2_hr) > 12 or int(time2_hr) <= 0:
                            raise ValueError
                        else:
                            new_time2_mins = str(time2_mins)
                            new_time2_mins = new_time2_mins.strip(" AM")
                            if int(time2_hr) == 12:
                                new_time2 = f"00:{new_time2_mins}"
                            elif int(time2_hr) == 11:
                                new_time2 = f"11:{new_time2_mins}"
                            elif int(time2_hr) == 10:
                                new_time2 = f"10:{new_time2_mins}"
                            elif int(new_time2_mins) >= 60:
                                raise ValueError
                            else:
                                if len(str(time2_hr)) == 2:
                                    new_time2 = f"{time2_hr}:{new_time2_mins}"
                                elif len(str(time2_hr)) == 1:
                                    new_time2 = f"0{time2_hr}:{new_time2_mins}"

                    return f"{new_time1} to {new_time2}"

        # IF FORMAT IS: 11:30 AM to 11 AM
        elif re.search(r"^(\d+):(\d{2})\s(?:AM|PM)\sto\s(\d+)\s(?:AM|PM$)", hours):
            new_hours = hours.split(" to ")
            long_time = new_hours[0]
            short_time = new_hours[1]
            long_time = str(long_time)
            new_long_time = long_time.split(":")
            long_hour = new_long_time[0]
            if int(long_hour) > 12 or int(long_hour) <= 0:
                raise ValueError
            long_mins_ampm = new_long_time[1]

            if "PM" in long_mins_ampm:
                new_long_hour = int(long_hour) + 12
                new_long_mins = str(long_mins_ampm)
                new_long_mins = new_long_mins.strip(" PM")
                if int(new_long_mins) >= 60:
                    raise ValueError
                elif new_long_hour == 12:
                    ans1 = f"12:{new_long_mins}"
                elif new_long_hour == 11:
                    ans1 = f"23:{new_long_mins}"
                elif new_long_hour == 10:
                    ans1 = f"22:{new_long_mins}"

                if len(str(new_long_hour)) == 2:
                    ans1 = f"{new_long_hour}:{new_long_mins}"
                elif len(str(new_long_hour)) == 1:
                    ans1 = f"0{new_long_hour}:{new_long_mins}"

            elif "AM" in long_mins_ampm:
                new_long_mins = str(long_mins_ampm).strip(" AM")
                if int(new_long_mins) >= 60:
                    raise ValueError
                elif long_hour == 12:
                    ans1 = f"00:{new_long_mins}"
                elif long_hour == 11:
                    ans1 = f"11:{new_long_mins}"
                elif long_hour == 10:
                    ans1 = f"10:{new_long_mins}"
                if len(str(long_hour)) == 2:
                    ans1 = f"{long_hour}:{new_long_mins}"
                elif len(str(long_hour)) == 1:
                    ans1 =f"0{long_hour}:{new_long_mins}"

            # CONVERT NUM2 PM
            if "PM" in short_time:
                new_short_time = str(short_time).split(" ")
                new_short_time = new_short_time[0]
                if int(new_short_time) > 12 or int(new_short_time) <= 0:
                    raise ValueError
                elif new_short_time == 12:
                    ans2 = f"12:00"
                elif new_short_time == 11:
                    ans2 = f"23:00"
                elif new_short_time == 10:
                    ans2 = f"22:00"
                new_short_time = int(new_short_time) + 12
                if len(str(new_short_time)) == 2:
                    ans2 = f"{new_short_time}:00"
                elif len(str(new_short_time)) == 1:
                    ans2 = f"0{new_short_time}:00"


            # CONVERT NUM2 AM
            elif "AM" in short_time:
                new_short_time = str(short_time).split(" ")
                new_short_time = new_short_time[0]
                if int(new_short_time) > 12 or int(new_short_time) <= 0:
                    raise ValueError
                elif new_short_time == 12:
                    ans2 = f"00:00"
                elif new_short_time == 11:
                    ans2 = f"11:00"
                elif new_short_time == 10:
                    ans2 = f"10:00"
                if len(str(new_short_time)) == 2:
                    ans2 = f"{new_short_time}:00"
                elif len(str(new_short_time)) == 1:
                    ans2 = f"0{new_short_time}:00"

            return f"{ans1} to {ans2}"

        # IF FORMAT IS: 11 AM to 11:30 AM
        elif re.search(r"^(\d+)\s(?:AM|PM)\sto\s(\d+):(\d{2})\s(?:AM|PM)$", hours):
            new_hours = str(hours).split(" to ")
            short_time = new_hours[0]
            long_time = new_hours[1]

            if "AM" in short_time:
                new_short_time = short_time.strip(" AM")
                new_short_hour = new_short_time
                if int(new_short_hour) > 12 or int(new_short_hour) <= 12:
                    raise ValueError
                elif new_short_hour == 12:
                    ans1 = f"00:00"
                elif new_short_hour == 11:
                    ans1 = f"11:00"
                elif new_short_hour == 10:
                    ans1 = f"10:00"
                if len(str(new_short_hour)) == 2:
                    ans1 = f"{new_short_hour}:00"
                elif len(str(new_short_hour)) == 1:
                    ans1 = f"0{new_short_hour}:00"

            elif "PM" in short_time:
                new_short_time = short_time.strip(" PM")
                short_hour = new_short_time
                if int(short_hour) > 12 or int(short_hour) <= 0:
                    raise ValueError
                elif short_hour == 12:
                    ans1 = f"12:00"
                elif short_hour == 11:
                    ans1 = f"23:00"
                elif short_hour == 10:
                    ans1 = f"22:00"
                else:
                    new_short_hour = int(short_hour) + 12
                    if len(str(new_short_hour)) == 2:
                        ans1 = f"{new_short_hour}:00"
                    elif len(str(new_short_hour)) == 1:
                        ans1 = f"0{new_short_hour}:00"

            if "AM" in long_time:
                new_long_time = str(long_time)
                new_long_time = new_long_time.strip(" AM")
                new_long_time = new_long_time.split(":")
                long_hour = new_long_time[0]
                if int(long_hour) > 12 or int(long_hour) <= 0:
                    raise ValueError
                else:
                    long_mins = new_long_time[1]
                    if int(long_mins) >= 60:
                        raise ValueError
                    elif long_hour == 12:
                        ans2 = f"00:{long_mins}"
                    elif long_hour == 11:
                        ans2 = f"11:{long_mins}"
                    elif long_hour == 10:
                        ans2 = f"10:{long_mins}"
                    if len(str(long_hour)) == 2:
                        ans2 = f"{long_hour}:{long_mins}"
                    elif len(str(long_hour)) == 1:
                        ans2 = f"0{long_hour}:{long_mins}"


            elif "PM" in long_time:
                new_long_time = str(long_time)
                new_long_time = new_long_time.strip(" PM")
                new_long_time = new_long_time.split(":")
                long_hour = new_long_time[0]
                if int(long_hour) > 12 or int(long_hour) <= 0:
                    raise ValueError
                else:
                    long_mins = new_long_time[1]
                    if int(long_mins) >= 60:
                        raise ValueError
                    elif long_hour == 12:
                        ans2 = f"12:{long_mins}"
                    elif long_hour == 11:
                        ans2 = f"23:{long_mins}"
                    elif long_hour == 10:
                        ans2 = f"22:{long_mins}"
                    else:
                        new_long_hour = int(long_hour) + 12
                        if len(str(new_long_hour)) == 2:
                            ans2 = f"{new_long_hour}:{long_mins}"
                        elif len(str(new_long_hour)) == 1:
                            ans2 = f"0{new_long_hour}:{long_mins}"

                return f"{ans1} to {ans2}"

if __name__ == "__main__":
    main()
