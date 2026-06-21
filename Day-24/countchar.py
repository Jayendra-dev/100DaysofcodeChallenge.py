# count characters in a file
with open("file.txt","r") as file:
    data=file.read()
print("total characters:",len(data))
