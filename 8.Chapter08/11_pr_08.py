# 8. Write a python function to print the multiplication table of a given number.
# def print_table(num):
    
def print_table(n):
    for i in range(1, 11):
  # print(str(num) + " X " + str(i) + "=" +str(i*num))
       print(f"{n} x {i} = {n*i}") # where 'f' is Formatted string litterels

n = int(input("Enter the num :"))
print_table(n)