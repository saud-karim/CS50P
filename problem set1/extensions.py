fileName = input("File name: ").strip()

indexDot = fileName.find(".")

if fileName[indexDot+1:] == "jpg" or fileName[indexDot+1:] == "jpeg":
    print("image/jpeg")
elif fileName[indexDot+1:] == "gif":
    print("image/gif")
elif fileName[indexDot+1:] == "png":
    print("image/png")
elif fileName[indexDot+1:] == "pdf":
    print("application/pdf")
elif fileName[indexDot+1:] == "txt":
    print("image/txt")
elif fileName[indexDot+1:] == "zip":
    print("image/zip")
else:
    print("application/octet-stream")
