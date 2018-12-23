d={}
n=int(input("enter no of employees: "))
i=1
while i<=n:
    name=input("enter employee name :")
    sal=input("enter emp sal:")
    d[name]=sal
    i=i+1
print("Name of employee" , "\t", "sal")
for x in d:
    print("\t",x,"\t\t",d[x])