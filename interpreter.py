expression = input("Expression: ").strip()

if "+" in expression:
    new_x = expression.split("+")
    sum = int(new_x[0]) + int(new_x[1])
    float_s = float(sum)
    print(float_s)

elif "-" in expression:
    new_x2 = expression.split("-")
    difference = int(new_x2[0]) - int(new_x2[1])
    float_d = float(difference)
    print(float_d)

elif "*" in expression:
    new_x3 = expression.split("*")
    product = int(new_x3[0]) * int(new_x3[1])
    float_p = float(product)
    print(float_p)

elif "/" in expression:
    new_x4 = expression.split("/")
    quotient = int(new_x4[0]) / int(new_x4[1])
    float_q = float(quotient)
    print(float_p)
