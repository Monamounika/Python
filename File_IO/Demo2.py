""" WITH keyword : with is a keyword in python
    Advantages:
    It'll TC of closing a file.
    After completing of all operations automatically even in case of exceptions also and we are not
    required to close explicitly.
"""

with open("input1.txt",'w') as f:
    f.write("welcome \n")
    f.write("Python World \n")
    print("Is file closed :", f.closed)
print("Is file closed :",f.closed)