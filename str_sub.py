'''Forword direction --> find(),index()
  Backword direction --> rfind(),rindex()'''


course="python programming language python"
#course=input("pls enter the string : ")
print(course.find("python"))
print(course.rfind("python"))
print(course.find("p",1,9))
print(course.find("p"))
print(course.index("p"))

'''In find() method if the sun string not found then we'll get -1 where as, in index() method we'll get ValueError
 so we can handle this error in app level'''
s="python programming language"
#print(s.index("hello"))
try:
    print(s.index("hello"))
except ValueError:
    print("not found")


s1="java programming language"
s2=s1.replace("java","python ")
print(s2)
print(s1)
print(id(s1))
print(id(s2))
n=s2.split()
print(n)
print(type(n))
for i in n:
    print(i)

c='-'.join(n)
print(c)