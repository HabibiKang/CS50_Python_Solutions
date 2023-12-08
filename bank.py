# implement a program that prompts the user for a greeting.
greet = input("Greeting: ").strip()
greet2 = list(greet)

# If the greeting starts with “hello”, output $0.
if "hello" in greet.lower():
     print("$0")

# If the greeting starts with an “h” (but not “hello”), output $20.
elif greet.startswith("h") and greet != "hello":
     print("$20")

elif greet.startswith("H") and greet != "hello":
     print("$20")
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
else:
     print("$100")
