# Find common elements between two lists
a=[10,20,30,40,50]
b=[30,40,50,60,70]
common=[]
for i in a:
    if i in b:
       common.append(i)
print(common)