"""1. Sequential stmts
   2. Conditional or Decision making stmts
   3. Loops
   4. Other -- > break,continue,return and pass
"""
"""
num=input("pls enter string :")

if num=='monu':
    print("hello",num)
elif num=="m":
    print("hello",num)
else:
    print("end")


name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!') """

"""First, the program sets the name variable u to an empty string. This is so
that the name != 'your name' condition will evaluate to True and the program
execution will enter the while loop’s clause v.
The code inside this clause asks the user to type their name, which
is assigned to the name variable w. Since this is the last line of the block,
the execution moves back to the start of the while loop and reevaluates the
condition. If the value in name is not equal to the string 'your name', then
the condition is True, and the execution enters the while clause again.
But once the user types your name, the condition of the while loop will
be 'your name' != 'your name', which evaluates to False. The condition is now
False, and instead of the program execution reentering the while loop’s
clause, it skips past it and continues running the rest of the program x.
If you never enter your name, then the while loop’s condition will never
be False, and the program will just keep asking forever. Here, the input()
call lets the user enter the right string to make the program move on. In
other programs, the condition might never actually change, and that can
be a problem.
"""



#for i in range(15,-1,-2):
 #   print (i)

#for j in range(10,0,-2):
 #   print(j)

#import random
#for i in range(5):
 #   print(random.randint(1, 10))
"""spam=int(input("enter num :"))
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings!    anything is fine.")



i=0
while i<=10:
    print(i)
    i+=1

num1=int(input("pls enter num1:"))
num2=int(input("pls enter num2 :"))
num3=int(input("pls enter num3 :"))

if (num1>num2) and (num1>num3):
    print(num1)
elif num2>num3:
    print(num2)
else:
    print(num3)

for i in range(1,5):
    for j in range(6):
        print("*",end=" ")
    print()

for i in range(4):
    for j in range(1,5-i):
        print(j,end=" ")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print() 

s=[4,5,8,3]
num=int(input("pls enter num :"))
for ele in s:
    if num==ele:
        print("found")
        break

else:
    print("not found")



weight = float(input("How many pounds does your suitcase weigh? "))
if weight > 50:
    print("There is a $25 charge for luggage and already deducted from your credit card, don’t get surprise.")
print("Thank you and Enjoy the Journey Boss.")



x="monu"
print(isinstance(x, int))
print(isinstance(x, str))




x=10
if isinstance(x, str):
    print("Yes it is integer type")
else:
    print("I am sure, it is not integer type")



name="monu"
if isinstance(name, int):
    print("Yes it is integer type")
else:
    print("I am sure, it is not int type")


allowed_users = ['Monu', 'Krishna', 'Vinni']
username = input("What is your login name? : ")
if username in allowed_users:
    print("Access granted, Enjoy Guru ")
else:
    print("Sorry Boss, access denied: Contact Admin team. Namaskaar")


for x in range(1, 20):
    if (x%2==0) and (x%4==0):
        print(x)


lines = []
print(lines)
while True:
    l = input()
    if l:
        lines.append(l)
    else:
        break
print(lines)


s = input("Enter string, mixed with numbers: ")
l=0
for c in s:
    if c.isdigit(): #isalpha()
        l=l+1
print("Characters count from entered text: ", l)


n = int(input("Enter a number for table: "))
for i in range(1,11):
    print(n, 'x', i,'=',n*i)

#x = [1,5,8]
#for i in x:
 #   print(i.upper())


i = 1
while i<=20:
    if i%3 == 0:
        break
    print(i)
    i += 2



#True = False
#while True:
 #   print(True)
  #  break

x = "python"
for i in x:
    print(i+"z")

x = "python"
while i in x:
    print(i)


x = "python"
i= "a"
while i in x:
    print(i)

x = 'abcd'
for i in range(10):
    print(i)

x = 'abcd'
for i in range(len(x)):
    print(i)

x = 'abcd'
for i in range(len(x)):
    #print(i[x]) TypeError : int object is not subsciptable
    print(x[i])

for i in range(2):
    print(i)

for i in " ":
    print(i)
"""
x = 2
for i in range(x):
    x -= 2
    print (x)

for i in range(9):
    if i == 5:
       break
    else:
        print(i)
else:
    print("no value")

text = "my name is python"
for i in text:
    print (i, end="")