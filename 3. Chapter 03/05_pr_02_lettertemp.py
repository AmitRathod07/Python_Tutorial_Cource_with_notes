letter =  '''Dear <|Name|>,
You are slected!
Date: <|DATE|>
'''

name = input("Enter your name \n")
date = input("Enter date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)
