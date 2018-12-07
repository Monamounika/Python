num = int(input("pls enter number:"))

fact=1
#if num == 0:
 #   print("factorial of 0 is 1")

for i in range(1,num+1):
    fact=fact*i
print("The factorial of", num, "is",fact)
