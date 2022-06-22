# 5. Repeat program 4 for a list of such words to be censored.
words = ["donkey", "patlu", "kaddu"]

with open('sample5.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@&**")    

with open("sample5.txt", "w") as f:
    content = f.write(content)

