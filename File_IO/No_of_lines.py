import os,sys

fname=input("enter file name:")
if os.path.isfile(fname):
    print("files exits :",fname)
    f=open(fname,'r')

else:
    print(fname,"file does exist")
    sys.exit(0) #to exit the system without executing rest of the program.

lcount=wcount=ccount=0

for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)

print("no.of line",lcount)
print("no.of words",wcount)
print("no.of characters:",ccount)

