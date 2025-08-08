extensions_type = str(input("File name: ")).strip().lower()


if extensions_type.endswith(".gif"):
   print("image/gif") 
elif extensions_type.endswith((".jpg",".jpeg")):
    print("image/jpeg")
elif extensions_type.endswith(".png"):
    print("image/png")
elif extensions_type.endswith(".pdf",):
    print("application/pdf")
elif extensions_type.endswith(".txt"):
    print("text/plain")
elif extensions_type.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
