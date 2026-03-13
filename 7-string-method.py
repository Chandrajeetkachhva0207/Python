#STRING METHODS (VERY IMPORTANT)

text1="    hello python learners     "

#Remove Spaces

# print(text1)
# print("Remove spaces:",text1.strip())  -->.strip() it is use to remove the unwanted space

# #Convert to capital letter

# print("capital letters:",text1.upper().strip())

# #Convert into Proper Case

# print("Proper letters:",text1.title().strip())

# #Convert into Lower Case
# print("Proper letters:",text1.lower().strip())

# #Replace
# print("Replcace python word",text1.replace("python","SQL"))

# #Count occurrences of a letter of word
# print("count of O",text1.count("o"))

#Check if text start with something

print("Start with hello?",text1.strip().startswith("hello"))

#check if only numbers are present int data

# mobile="988849459"
# print("is numeric :",mobile.isnumeric())

#Split string into list of words

msg="welcome to python course"
# words=msg.split()
# print("word list :",words)

#join back with hypen

# joined_text="-".join(words)
# print("join text:",joined_text)

#find the position of letter
print("index of letter :",msg.find("p"))

#Extract Domain
email="chandrajeetkachhva@gmail.com"
domain=email[email.find("@")+1:]
print("Domain :"+domain)



