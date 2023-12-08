import sys

from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


elif ".jpg" not in sys.argv[2] and ".png" not in sys.argv[2] and ".jpeg" not in sys.argv[2]:
    sys.exit("Invalid output")

elif ".jpg" in sys.argv[1] and ".jpg" not in sys.argv[2]:
    sys.exit("Input and output have different extensions")

elif ".png" in sys.argv[1] and ".png" not in sys.argv[2]:
    sys.exit("Input and output have different extensions")

elif ".jpeg" in sys.argv[1] and ".jpeg" not in sys.argv[2]:
    sys.exit("Input and output have different extensions")


elif len(sys.argv) == 3:
    try:
        input_img = Image.open(sys.argv[1]) # opens input image
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png") # opens shirt image
    size = shirt.size # get shirt size
    input_img = ImageOps.fit(input_img, size) # assign that size to input image
    input_img.paste(shirt, shirt) # paste shirt onto input image
    input_img.save(sys.argv[2]) # save second command line arg file




