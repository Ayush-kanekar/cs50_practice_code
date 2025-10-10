import sys 
from pyfiglet import Figlet 

text = input("input:")
f = Figlet()
if sys.argv[1] == "-f" or sys.argv[1] == "--font":
    f.setFont(font= sys.argv[2])
    print(f.renderText(text))
