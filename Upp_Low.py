#stringMixCap="outofmemoryerror"

stringMixCap=input("pls enter the word :")
acc=''
for num,i in enumerate(stringMixCap):
 if num % 2 == 0:
  acc+=i.upper()
 else:
  acc+=i.lower()
print(acc)
