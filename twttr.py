def main():
    word1 = input("Input: ")
    print(shorten(word1))

puncts = "+_*$#%@<>,.:"

def shorten(word2):
    vowels = ["a", "e", "i", "o", "u"]
    ans = ""
    for character in word2:
        if character.lower() not in vowels:
            ans += character
    return(ans)


if __name__ == "__main__":
    main()
