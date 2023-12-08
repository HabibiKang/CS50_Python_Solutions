def my_cat():
    cuteness = 0
    name = "habibi"
    username = str(input("Enter kitty name: "))
    if name != username:
        cuteness -= 1
        return cuteness
    elif name == username:
        cuteness += 1
        return cuteness

    if __name__ == "__main__":
        my_cat()

