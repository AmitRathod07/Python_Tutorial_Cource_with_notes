story = "Once apone atime a student learn python from youtuber code weith harry"

#string functions
print(len(story)) #want to know length of the story string
print(story.endswith("harry")) #string.endwith(ending text) #wants to know which latter ends with...
print(story.count("a")) #string.count(character) #mostly found character in story and also find the number of the string in the story
print(story.capitalize()) #story.capitalixe() #This function capitalize the first character of a given string...
print(story.find("once")) #string.find(word) #This function finds a word and returns the index of first occurence of that word in the string...
print(story.replace("Harry", "Codewithharry")) #string.replace(oldword, newword) #This function replaces the oldword with newword in the entire string.

#                               Escape sequence characters
# Sequence of character after backslash '\'  
# Escape seq. ch. compaire of more rhan one characters but represents one character when used within the strings.

#Examples:

# \n -> For newline 
# \t -> Tab
# \' -> Singlequate
# \\ -> backslash 

StoryA = "Amit is good.\nHe \tis ve\\ry good"
print(StoryA)


