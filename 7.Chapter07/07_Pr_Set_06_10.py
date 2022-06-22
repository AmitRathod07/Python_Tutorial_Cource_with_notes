# 6 Write a program to calculate the factorial of a given number using for loop.
# n! = 1 x 2 x 3 x 4 x 5 x.....x n = n*(n+1)
# 5! = 1 x 2 x 3 x 4 x 5

num=int(input("Enter a number:"))
Fact = 1
for i in range(1, num+1):
    Fact = Fact * i
print(f"The factorial of this number is {Fact}")

# 7 Write a program to print the following star pattern.
'''
    *
   ***  
  ***** for n=3
'''

n = 3
print("The Pattern is:")
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
# 8 
# Write a program to print the following star pattern:
'''
*
**
*** for n = 3
'''

n = 4
print("The Pattern is:")
for i in range(4):
    print("*" * (i+1))

# 9 Write a program to print the following star pattern:
'''
* * *
*   *             #For n=3
* * * 
'''

n=3 
for i in range (3) :
    for j in range(3) :
            if(i==0 or i ==n-1 or j==0 or j==n-1) :
               print("*", end=" ") 
            else:
                print(" ", end=" ") 
    print() 


# 10 Write a program to print the multiplication table of n using for loop in reversed order.

n = int(input("Enter the num :"))
for i in range(11,0,-1):
  # print(str(num) + " X " + str(i) + "=" +str(i*num))
  print(f"{n}x{i}={n*i}")


