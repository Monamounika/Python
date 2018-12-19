#Define punctuations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
word=input("pls enter the sentense :")
# remove punctuation from the string
no_punct = ""
for char in word:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)