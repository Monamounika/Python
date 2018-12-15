"""num1=int(input("please enter num1:"))
num2=int(input("pls eter num2 :"))
if num1"""

def Gcd(a,b):
    if b==0:
        return a

    else:
        return Gcd(b,a%b)
num1=int(input("please enter num1:"))
num2=int(input("pls eter num2 :"))
print(Gcd(num1,num2))

num3=num1*num2
for i in range(1,num3):
    if (i%num1==0 and i%num2==0):
        break
print("lcm of 2 nums is :",i)
