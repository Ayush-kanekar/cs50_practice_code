def main():
    text = str(input())
    print(convert(text))

def convert(emoji):
    return emoji.replace(":)","🙂" ).replace(":(","🙁")

main()



