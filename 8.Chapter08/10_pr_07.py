# 7. Write a python function to remove a given word from a string and strip it at the same time.
def remove_and_split(string, word):
    newStr=string.replace(word, "")
    return newStr.strip()

this = "    Amit is a student   "
n=remove_and_split(this, "Amit")
print(n)
# print(this)
# print(this.strip())

