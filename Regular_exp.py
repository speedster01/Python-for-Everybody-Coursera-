import re
fname=input("Enter the file name: ")
fh=open(fname)

sum=0

for line in fh:
    y=re.findall('([0-9]+)',line)
    for i in y:
        sum+=int(i)

print(sum)
