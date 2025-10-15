import sys 
import random
from pyfiglet import Figlet 
sub_commands =["-f","--fonts"]
figlet = Figlet()
if len(sys.argv) == 1 :
    font =random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    text = input("input: ")
    print("Output:")
    print(figlet.renderText(text))
    sys.exit()

elif len(sys.argv) == 3 and sys.argv[1] in sub_commands:
    print(sys.argv[1])
#check if the font is avaliable from sys.argv[2]
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
#take user input
        text = input("input: ")
        print("Output:")
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
