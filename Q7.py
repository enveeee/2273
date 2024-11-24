import string
input_str=input("Enter the input string which contains punctuations:")
#REMOVE PUNCTUATIONS
nopunc=""
for char in input_str:
    if char not in string.punctuation:
        nopunc=nopunc+char
print(nopunc)
