# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13- year old boy.
for g in range(2, 21):
    with open(f"Tables/Multiplication_table_of_{g}.txt", "w") as f:
        for h in range(1, 11):
            f.write(f"{g}x{h}={g*h}") #F string
            if h!=10:
                f.write('\n')
        
        
            
