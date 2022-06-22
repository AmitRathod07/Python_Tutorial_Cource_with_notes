# 11. Write a python program to rename a file to “renamed_by_python.txt.”
import os 

oldname = "Sample2.txt" 
newname = "renamed_by_python.txt"

with open(oldname) as g:
    content = g.read()
with open(newname, "w") as g:
    g.write(content)

os.remove(oldname) #delete the file after renming