# count total words in a file
with open("file.txt","r") as f:
    data=f.read()
words=data.split()
print("total words:",len(words))    
