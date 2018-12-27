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


s1="hello"
s2="hello"
s3="hi"
print(s1 == s2)
print(s2 == s3)

print("abcd"[2:])

str1 = '\nhe\nllo'
print(str1)

print("\nh\ne\nl\nl\no")
print('new' 'line')
#xample = "snow world"
#xample[3] = 's'
#rint(example)

l="hello wahh qu"
print(max(l))
print(min(l))

q="what are you doing"
print(max(q))
print(min(q))

example="hello"
print(example.count("l"))

example = "helle"
print(example.find("e"))
print(example.rfind("e"))


example="helloworld"
#rint(example[::0]) ValuError : Slice step cannot be zero


str1="restart"
char = str1[0]
str1 = str1.replace(char, '$')
print(str1)



str1="restart"
char = str1[0]
str1 = str1.replace(char, '$')
str2 = char + str1[1:]
print(str2)


example="helloworld"
print(example[::-1].startswith("d"))
print(example.startswith("d"))

print("hello\example\test.txt")

print("hello\\example\\test.txt")

print("hello\”example\”test.txt")
print("hello”\example”\test.txt")
#print(“hello”+1+2+3)
print("D", end = ' ')
print("C", end = ' ')
print("B", end = ' ')
print("A", end = ' ')
print("Hello".replace("l", "e"))
print("abc DEF".capitalize())
print("ABCDEF".upper())
#print("abcdef".center())
print("xyyzxyzxzxyy".count('yy'))
print("xyyzxyzxzxyy".count('yy', 4))
print("Hello {0} and {1}".format('foo', 'bin'))
print("Hello {1} and {0}".format('bin', 'foo'))
print("Hello {} and {}".format('foo', 'bin'))
#print("Hello {name1} and {name2}".format('foo', 'bin'))
print("Hello {name1} and {name2}".format(name1='foo', name2='bin'))
print('The sum of {0} and {1} is {2}'.format(2, 10, 12))
print('ab12'.isalnum())
print('ab,12'.isalnum())
print('ab'.isalpha())
print('a B'.isalpha())
print(''.isdigit())
print('my_string'.isidentifier())
print('11'.isnumeric())
print('HelloWorld'.istitle())
print('Hello World'.istitle())
print('Hello World'.title())

print('abcdef'.partition('cd'))
print('abcdefcdgh'.partition('cd'))
print('abcd'.partition('cd'))
print('abef'.replace('cd', '12'))
print('abef'.replace('ab', '12'))
print('abcdefcdghcd'.split('cd'))
print('Ab!2'.swapcase())