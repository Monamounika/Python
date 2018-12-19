"""group=[2,4,6,8,1]
search = int(input("pls enter the num : "))
for element in group:
    if search==element:
        print("num found",element)
        break
else:
    print("couldn't find")

loc = sap
       blg"""

course="python practice  "
print(course.find("python"))
print(course.find("Python"))

count = 0
word=input("enter word :")
search=input("enter the letter ehich u want to search :")
for letter in word:
    if(letter == search):
        count += 1
print(count,'letters found')