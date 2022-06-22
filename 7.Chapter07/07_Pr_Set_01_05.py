# 1 Write a program to print the multiplication table of a given number using for loop.
num = int(input("Enter the num :"))
for i in range(1, 11):
  # print(str(num) + " X " + str(i) + "=" +str(i*num))
  print(f"{num}x{i}={num*i}")

# 3 Problem 1 using while loop 
'''
j=0
while j>=1 and j<=11 :             my trial
  j = j + 1
  print(f"{num}x{j}={num*j}")'''

a=int(input("enter table number:"))
b=int(input("enter the number to which table is to printed:"))
i=1
while i<=b:
    print(a,"x",i,"=",a*i)
    i=i+1

# 2 Write a program to greet all the person names stored in a list l1 and which starts with S.
l1 = ["Harry", "Sohan", "Sachin", " Rahul"]

for name in l1:
  if name.startswith("S"):
    print("Hemlo hemloo " + name)

# 4 Write a program to find whether a given number is prime or not.
 
num = int(input("Enter the num :"))
prime=True
for i in range(2, num):
  if(num%i == 0):
    prime = False
    break
if prime:
  print("This number is prime.")
else:
  print("This num is not prime.")
    
# 5 Write a program to find the sum of first n natural numbers using a while loop.
n=int(input("Enter a number:"))
if n<0:
  print("Enter a posiitive number")
else:
  sum1=0
  while(n>0):
    sum1 = sum1 + n
    n = n-1 
  print("The sum of first n natural numbers is :", sum1)


