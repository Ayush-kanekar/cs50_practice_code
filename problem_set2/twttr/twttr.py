vowels = ['A','a','E','e','I','i','O','o','U','u']
texts = str(input("Input: "))
print("Output: ",end="")
for text in texts:
    if text not in  vowels:
        texts.replace(text,"")
        print(f"{text}",end="")
    
