# n! = 1 * 2 * 3 * 4 * 5 *....* N (N=Natural Numbers)
# n! = [1 * 2 * 3 * 4 * 5 *....* (N-1)] * N
# n! = N * (N-1)!

# n = 0
# #n = input(print("Enter factorial num: "))
# product=1
# for i in range(n):
#     product = product * (i+1)
# print(product)

# With Function
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

# With Function cursion

def factorial_recursive(n):
    if n == 1 or n == 0: # <-- Base condition which deosn't call the fun. any further
        return 1
    return n * factorial_recursive(n-1)

# f=factorial_iter(0)
f = factorial_recursive(0)
print(f)

# Recursion is function call 
'''
This works as follows :
    Factorail(4)--> Function called
      |          
     4 *  Factorial(3)
     4 *   [3 X factorial(2)]
     4 * 3 * [2 X factorial(1)]  
     4 * 3 * 2 * [1] [Function return]
'''
'''
The programmer need to be extremely careful while working with recursion to ensure that the fumetion doesn't Infinitely keep calling itself. 
Recursion is sometimes the most direct way to code on algorithm
'''



