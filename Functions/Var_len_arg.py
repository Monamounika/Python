'''
    The variable length argv is an argv that can accept any no.of values.
    The variable length argv is written with * before variable in fn definition.
'''

def totalcost(x,*y):
    sum=0
    for i in y:
        sum+=i
    print(x+sum)
    #print(sum)
totalcost(100,200)
totalcost(122,576,8)
totalcost(67)

def totalmul(x,*y):
    mul=1
    for i in y:
        mul*=i
    print(x*mul)
totalmul(10,20)
totalmul(122,576,8) #here x=122 and y=576,8(stored in tuple).
totalmul(90)

#keyword length argument Internally it represents like a dict object.

def kwargs(**kw):
    print(kw)
kwargs(id=8,name="monu")
kwargs(id=9,name="maha",quali="BCA")
#kwargs(6,"kill")  TypeError: kwargs() takes 0 positional arguments but 2 were given
