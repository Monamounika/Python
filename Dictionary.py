d={}
n=int(input("enter no of employees: "))
for i in (1,n+1):
#i=1
#while i<=n:
    name=input("enter employee name :")
    sal=input("enter emp sal:")
    d[name]=sal
 #   i=i+1
print("Name of employee" , "\t", "sal")
for x in d:
    print("\t",x,"\t\t\t\t",d[x])