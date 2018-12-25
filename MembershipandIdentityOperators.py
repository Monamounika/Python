#Membership operators

# in and not in, in-->T if the element found in collection.
#   not in -->T if the element not found in the collection.

text="python programming language"
print("welcome" in text) #F
print("python" in text) #T
print("python" not in text) #F
print("welcome" not in text) #T

# Identity operators  --> compares the m/m location of two objects.

# is, is not
# is  --> A and B True, if both A & B are pointing to the same object.
# is not --> A and B True, if both A & B are not pointing to the same object.

a=10
b=10
print(a is b) #T
print(a is not b) #F