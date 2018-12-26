'''Forword direction --> find(),index()
  Backword direction --> rfind(),rindex()'''


course="python programming language python"
#course=input("pls enter the string : ")
print(course.find("python"))
print(course.rfind("python"))
print(course.find("p",1,9))
print(course.find("p"))
print(course.index("p"))

'''In find() method if the sun string not found then we'll get -1 where as, in index() method we'll get ValueError '''
s="python programming language"
#print(s.index("hello"))
try:
    print(s.index("hello"))
except ValueError:
    print("not found")