 # Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import string
import random

def random_char(y): # This method is used to import random characters
    return ''.join(random.choice(string.ascii_letters)for x in range(y))

st = input("Enter the message: ")
words = st.split(" ") # this method splits the string into a list
coding = input("Enter 1 for Coding 0 for Decoding: ")
coding = True if coding == "1" else False  # short hand if else statements
if(coding):
    nwords = [] # an empty list
    for word in words:
        if(len(word) >= 3):
            r1 = random_char(3) # calling that random_char funtion
            r2 = random_char(3)     
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1]) # To reverse a string
    print(" ".join(nwords))
else:
    nwords = [] # an empty list
    for word in words:
        if(len(word) >= 3):   
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:   
             nwords.append(word[::-1]) # To reverse a string
    print(" ".join(nwords))


