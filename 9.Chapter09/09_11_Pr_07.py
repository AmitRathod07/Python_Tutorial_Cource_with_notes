# 7. Write a program to find out the line number where python is present from question 6.
content = " "
i = 1
with open("Log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line num {i}")
        i+=1