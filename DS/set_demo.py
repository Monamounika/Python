s={1,"maha",85,"monu",67,85}
print(s)
#s[0]="Krishna" TypeError: 'set' object does not support item assignment
#print(s[0])   TypeError: 'set' object does not support indexing

s.add(50)
print(s)


s={}
print(s)
print(type(s))  #<class 'dict'>

s=set()
print(s)
print(type(s)) #<class 'set'>

s.add(50)
print(s)