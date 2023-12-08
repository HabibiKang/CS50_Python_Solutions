text = input("Enter a string: ")

def convert(text):
    if ":)" in text and ":(" not in text:
        new_text = text.replace(":)", "🙂")
        print(new_text)

    elif ":(" in text and ":)" not in text:
        new_text = text.replace(":(", "🙁")
        print(new_text)

    elif ":)" in text and ":(" in text:
        new_text = text.replace(":)", "🙂").replace(":(", "🙁")
        print(new_text)

    return new_text

convert(text)
