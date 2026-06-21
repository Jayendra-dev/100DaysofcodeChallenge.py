# count characters in a file
with open("file.py","r") as file:
    data=file.read()
print("total characters:",len(data))
