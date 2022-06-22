#Use open function to content of the file
# f = open('Sample.txt', 'r')
f = open('Sample.txt', 'r') #By drfault the mode is r
# data = f.read()
data = f.read(5) # Reads FIRST FIVE CHARS FROM THE FILE
print(data)
f.close()

