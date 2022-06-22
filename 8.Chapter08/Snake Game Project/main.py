# After The Chapter 08 this project is performed amit
'''
We all have played snake, water gun game in our childhood. If you haven’t, 
google the rules of this game and write a Python program capable of playing this game with the user.
'''

# Rules
'''
Snake water and gun
like rock papper and scissors

gun kill snake
water absorb gun
snake drink water

'''


import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("com Turn: Snake(s) watre(w) or Gun(g) ?")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'



you = input("your Turn: Snake(s) watre(w) or Gun(g) ?")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"Computer choose {you}")

if a == None:
    print("The Game Is Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")


