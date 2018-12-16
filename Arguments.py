"""def Details(item,price):
    print(item,"cost is :",price)
Details(item='bangles',price=500)
Details('Shirt',1000)
#Details(item='bangles',500)"""


#variable length argument
def totalcost(x,*y):
    sum=0

    for i in y:
        sum+=i
    print(x + sum)
totalcost(100)
totalcost(100,200,300)

def totalsub(a,*b):
    sub=0
    for j in b:
        sub-=j

    print(a+sub)
totalsub(200)
totalsub(900,600,800)
totalsub(200,300)