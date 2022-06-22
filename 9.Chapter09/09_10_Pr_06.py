# 6. Write a program to mine a log file and find out whether it contains ‘python’.
with open("Log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present")
else:
    print("No Python is not present")