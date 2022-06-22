#greeting = "Good Morning"
#name = "Amit" # name="|A |m |i |t |" --> length = 4
               #       |0 |1 |2 |3 | 
               #       |-5|-4|-2|-1
              
# print(type(name))
# Concatenating two strings
# c = greeting + name
#print(c)
# -------------------------------------------------
# if we want A&m from name="Amit"
name = "Amit"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
#name[3] = "d" --> Does not work to chang string


print(name[1:3]) #print(name[0:3]) use also...
print(name[:2])  # is same as name[0:2]
print(name[2:])  # is same as name[2:4] 
c = name[-4:-1]  # is same as name[1:4]
print(c)

#slicing with skip value
d = name[1:4:1]
print(d)





