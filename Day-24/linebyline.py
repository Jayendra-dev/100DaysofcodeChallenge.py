# write a program to read a file line by line
f=open("file.txt","r")
for line in f:
    print(line.strip())
f.close()
