def cart(item,price):
    print(item,"cost is :",price)

cart(item="Bangles",price=900)
cart(price=453,item="Shirt")
cart("Saree",price=777) #positional argument follows keyword arguments
cart("soley",900)
cart(900,"soley")

#Default Arguments

def cart(item,price=455):
    print(item,"cost is :",price)
cart("soley")
cart("Salwar",45)

'''SyntaxError: non-default argument follows default argument

def m(a=10,b):
    print(a)
    print(b)
m(40,50)

'''


