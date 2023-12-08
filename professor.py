from random import choice
from random import randint

def main():
    score = 0
    problem_count = 10
    attempts = 3
    level = get_level()
    while problem_count != 0:
        if attempts == 3:
            num1, num2 = generate_integer(level)
        try:
            guess = int(input(f"{num1} + {num2} = "))
            ans = num1 + num2
            if guess == ans:
                problem_count -= 1
                score += 1
                attempts = 3
                continue
            else:
                raise ValueError
        except ValueError:
            print("EEE")
            attempts -= 1
            pass
        if attempts == 0:
            print(f"{num1} + {num2} = {ans}")
            attempts = 3
            problem_count -= 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        num1 = randint(0, 9)
        num2 = randint(0, 9)
    elif level == 2:
        num1 = randint(10, 99)
        num2 = randint(10, 99)
    elif level == 3:
        num1 = randint(100, 999)
        num2 = randint(100, 999)
    return num1, num2

if __name__== "__main__":
    main()
