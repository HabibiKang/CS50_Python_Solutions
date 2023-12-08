prompt = input("Enter a file: ").lower().strip()

if prompt.endswith(".gif"):
    print("image/gif")

elif prompt.endswith(".jpg"):
    print("image/jpeg")

elif prompt.endswith(".jpeg"):
    print("image/jpeg")

elif prompt.endswith(".png"):
    print("image/png")

elif prompt.endswith(".pdf"):
    print("application/pdf")

elif prompt.endswith(".txt"):
    print("text/plain")

elif prompt.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
