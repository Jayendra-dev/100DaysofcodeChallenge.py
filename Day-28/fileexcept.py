# handle file not found exception.
try:
    file=input(" enter file name:")
    with open(file,"r") as f:
        print(f.read())
except FileNotFoundError:
    print("file do not found")
