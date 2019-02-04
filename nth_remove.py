s = input("pls enter the string:")
n = input("which character you want ot remove:")
c=-1
for i in s:
    c+=1
    if n==i:
        m = c
        break
print(s[:m]+s[m+1:])


