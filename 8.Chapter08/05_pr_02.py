# 2. Write a python program using the function to convert Celsius to Fahrenheit.

# (0°C × 9/5) + 32 = 32°F
def farh(cel):
    return (cel * (9/5)) + 32

c = 45
f = farh(c)
print("Fahrenhit temp is " + str(f))
