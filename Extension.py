file = input("please enter the files name :")
#print("file extension is :",file.split('.'))
s=file.split('.')
print("file extension is : ",repr(s[1]))
