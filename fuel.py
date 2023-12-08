def main():
    while True:
        try:
            fraction = input("Fraction: ")
            if "/" not in fraction:
                raise ValueError("Did not enter a fraction.")
            elif "/" in fraction:
                new = fraction.split("/")
                x = int(new[0])
                y = int(new[1])
                if y == 0:
                    raise ZeroDivisionError("Cannot divide by 0.")
                elif x > y:
                    raise ValueError

                elif x == y:
                    return x, y
            
                elif x == 2 and y == 3:
                    return x, y

                elif x < y:
                    convert(x,y)
                    break

        except ValueError:
            continue

def convert(x, y):
    q = float(x) / float(y) * 100
    new_q = str(q)
    new_q2 = float(new_q)
    new_q3 = int(new_q2)
    new_q4 = round(new_q3, 0)
    new_q5 = str(new_q4)
    final = new_q5.split(".")
    answer = final[0]
    if int(answer) <= 1:
        print(int(answer))
