#pr_03 To detect doublespaces
st = "this is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces) 

#pr_04  To detect single space
st = "this is a string with double   spaces"

st = st.replace("  ", " ")
print(st) 
