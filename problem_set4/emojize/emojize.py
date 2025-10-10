import emoji,sys
text = input("Input: ")
if "," in text:
    greating,emote = text.split(" ")
    print(greating,emote)
    if emote == ":earth_asia:":
        emote = emoji.emojize(":globe_showing_Asia-Australia:")
        print(f"output:{greating} {emote}")
        sys.exit()
    emote = emoji.emojize(emote)
    print("output:",greating,emote)
    sys.exit()
text = text.replace("thumbsup","thumbs_up")
emojis = emoji.emojize(text)
if text == ":smile_cat:":
    cat = emoji.emojize(":grinning_cat_with_smiling_eyes:")
    print(f"output: {cat}")
else:
    print(f"output:{emojis}")
