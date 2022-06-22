# 2. The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.

def game():
    return 8546

score = game()
with open("Hiscore.txt") as f:
    hiscorestr = f.read()
if hiscorestr == '':
    with open("Hiscore.txt", "w") as f:
        f.write(str(score)) 

elif int(hiscorestr)<score:
    with open("Hiscore.txt", "w") as f:
        f.write(str(score))   

