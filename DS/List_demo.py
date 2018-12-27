n=[1,2,3]
print(n[1])
n[1]=5
print(n[1])
print(n)

r=range(1,10)
l=list(r)
print(l)

print(l[::-1])

for x in l:
    print(x)

m=[]
m.append("monu")
m.append("maha")
m.append(1)
print(m)
m.insert(0,6)
print(m)
m.insert(1,"Rani")
print(m)

l1=[1,2,3]
l2=["Krishna","Hima"]
print("before extend l1 :",l1)
print("beforer extend l2:",l2)
#p=l2.extend(l1)
#print("after extend l1:",p  )
l2.sort()
print(l2)
#print(l2,l2.sort())

x=[10,20,30]
y = x  # 'y' is Alias name
print(x)
print(y)
print(id(x))
print(id(y))
y.append(40)
print(x)
print(y)

#cat = ['fat', 'black', 'loud']
cat = ["size","color","disposition"]
print(cat)

x=[10,30,50]
y=x[:] #cloning
print(x)
print(y)
print(id(x))
print(id(y))
y.append(40)
print(x)
print(y)

#Nested lists

m=[6,8,9]
n=[1,2,3,m]
print(n)
