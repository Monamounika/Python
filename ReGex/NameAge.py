import re
#nameage = open("nameages.txt",'r') this one won't work

with open("nameages.txt",'r') as dummy:
    data = dummy.readlines()
#nameages = '''Monu is 67
 #and John is 46
 #Alove  is 45 and Alex is 23'''

age = re.findall(r'\d{1,3}',str(data))
name = re.findall(r'[A-Z][a-z]*',str(data))
ageDict = {}
x = 0
for eachname in name:
    ageDict[eachname] = age[x]
    x+=1

print(ageDict)
