from random import choice
from pyfiglet import Figlet
import sys
figlet = Figlet()

fonts = figlet.getFonts()
ran_font = choice(fonts)

while True:
    if len(sys.argv) == 1:
        prompt = input("Input: ").strip()
        figlet.setFont(font=ran_font)
        print(figlet.renderText(prompt))
        break

    if len(sys.argv) == 2:
        sys.exit("Invalid Usage")

    elif len(sys.argv) == 3:
        cmd1 = sys.argv[1]
        #sys.argv[1] make sys variables
        if cmd1 == "-f" or cmd1 == "--font":
            if sys.argv[2] in fonts:
                prompt = input("Input: ").strip()
                f = sys.argv[2]
                figlet.setFont(font=f)
                print(figlet.renderText(prompt))
                break

            # check to make sure sys2 is the name of the font
            elif sys.argv[2] not in fonts:
                sys.exit("Invalid Usage")

        else:
            sys.exit("Invalid Usage")
