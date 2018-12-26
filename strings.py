wrd=input("pls enter string :")
#print(wrd[5])
#print(wrd[-5])
print(len(wrd))
print(wrd[::-1])
print(wrd[::-2])
print(wrd[-4:-1])
print(wrd[4:9])

main=input("enter string :")
s=input("enter sub string :")
if s in main:
    print(s,"is found in main string")
else:
    print(s,"is not found in main str ")

m=" hello hi  "
x=m.strip()

z=m.lstrip()
y=m.rstrip()
print(len(m))
print(len(x))

print(len(z))
print(len(y))