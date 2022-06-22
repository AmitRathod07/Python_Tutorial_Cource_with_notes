# 4. A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.

with open('sample5.txt') as f:
    content = f.read()

content = content.replace("donkey", "$%^@&**")    

with open("sample5.txt", "w") as f:
    content = f.write(content)
