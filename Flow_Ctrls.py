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
"""
