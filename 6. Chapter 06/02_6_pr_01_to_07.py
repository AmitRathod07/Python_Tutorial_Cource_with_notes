

# --------------------
'''
Q1  Write a program to find the greatest of four numbers entered by the user.
Q2 Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
 Q3 A spam comment is defined as a text containing the following keywords:
“make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

Q4 Write a program to find whether a given username contains less than 10 characters or not.
Q5 Write a program that finds out whether a given name is present in a list or not.
Q6 Write a program to calculate the grade of a student from his marks from the following scheme:
90-100	Ex
80-90	A
70-80	B
60-70	C
50-60	D
<50	F
Q7 Write a program to find out whether a given post is talking about “Harry” or not.



'''

# Ans
# A1
'''
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
num3 = input("Enter number 3: ")
num4 = input("Enter number 4: ")

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num1

if(f1>f2):
    print(str (f2) + " is greatest")
else:
    print(str (f1) + " is greatest")
'''
#A2
'''
sub1 = int(input ("Enter First subject marks\n"))
sub2 = int(input ("Enter second subject marks\n"))
sub3 = int(input ("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail try again next time")

elif(sub1+dub2+sub3)/3 <40:
        print("You are fail due to total percentage less than 40")
else:
    print("Congretulations!!! You Passed The Exam")
'''

#A3

# text = input("Enter the text")
# spam = False

# if("make a lot of money"):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("whatch this" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")

#A4

# use lenght function

#A5
'''
names = ["vicky","tinku","sandy"]
name = input("Enter the name to check:\n" )
if name in names:
    print(str(name) + " - This name is present in the list")
else:
    print(str(name) + " - This name is not present in the list")
'''

# A6
''' convert marks to Grades 
marks = int(input("Enter Your Marks\n"))

if marks>90:
    grades = "Ex"
elif marks>=80:
    grades = "A"
elif marks>=70:
    grades = "B"
elif marks>=60:
    grades = "C"
elif marks>=50:
    grades = "D"
elif marks>=40:
    grades = "E"
else:
    grades = "F"

print("Your grade is " + grades)
'''

#Q7
# do as ditect characcterstring