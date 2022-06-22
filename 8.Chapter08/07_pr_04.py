#  4. Write a recursive function to calculate the sum of first n natural numbers.

# n! = n * (n-1)!
# sum(n) = sum(n-1) + n

# for first n line of sum 
# n = 1+2+3+... +n
# sum(n) = sum(1+2+3+...+n)
def recur_sum(n):
    if n<=1:
        return n
    else:
        return n + recur_sum(n-1)

N = 5

if N<0:
    print("Enter a positive number")
else:
    print("The sum is : ", recur_sum(N))

