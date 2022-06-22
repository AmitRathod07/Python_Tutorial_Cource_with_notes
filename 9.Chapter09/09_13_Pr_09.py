# Write a program to find out whether a file is identical and matches the content of another file.

file1 = "Log.txt"
file2 = "this.txt"

with open(file1) as g:
    f1 = g.read()

with open(file2) as d:
    f2 = d.read() 

if f1 == f2:
    print("This file are identical.")
else:
    print("This files are not identical.")


