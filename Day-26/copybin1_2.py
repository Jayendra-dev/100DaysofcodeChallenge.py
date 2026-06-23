# copy one binary file to another
with open("bin1file.bin","rb") as src:
    data=src.read()
with open("bin2file.bin","wb") as dst:
    dst.write(data)
print("file copied successfully")        
