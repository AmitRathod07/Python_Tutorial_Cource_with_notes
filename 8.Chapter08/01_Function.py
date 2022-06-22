marks=[45, 85, 95, 74, 95]
per1 = ((marks[0] + marks[1] + marks[2] + marks[3] + marks[4])/500)*100

marks2=[75, 98, 88, 78]
per2 = (sum(marks2)/400)*100
print(per1, per2 )

#per = percentage
 
# greet good day
def greet(name):
	gr = "Hello " + name
	return gr
a = greet(input("Enter the name :"))
print(a)

# Function with arguments
# all
# buildin function len(), print(), range(), sum()....etc.

def mySum(num1, num2):
	return num1 + num2 

greet("Harry")
s = mySum(6, 32)
print(s)