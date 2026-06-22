# program to replace a word in a file
with open("file.txt","r") as file:
    data=file.read()
data=data.replace("python","java")
with open("file.txt","w") as file:
    file.write(data)
print ("word replaced successfully")
