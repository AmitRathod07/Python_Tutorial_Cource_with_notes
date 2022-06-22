with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("me")
print(a)

# You don't have to close the file

