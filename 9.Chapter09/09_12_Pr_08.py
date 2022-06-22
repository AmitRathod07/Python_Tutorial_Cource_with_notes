# 8. Write a program to make a copy of a text file “this.txt.”
from typing import ContextManager


with open("this.txt") as f:
    Content = f.read()

with open("copy.txt", "w") as f:
    f.write(Content)


