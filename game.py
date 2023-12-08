from random import choice

while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            continue
        else:
            num = choice(range(n))
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess < 1:
                        continue
                    elif guess > n:
                        continue
                    elif guess > num:
                        print("Too large!")
                        continue
                    elif guess < num:
                        print("Too small!")
                        continue
                    elif guess == num:
                        print("Just right!")
                        exit()

                except ValueError:
                    continue
    except ValueError:
        continue
