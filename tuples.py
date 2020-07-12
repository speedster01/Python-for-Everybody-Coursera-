#Calculate the count of each hour on when mail has been sent and print this in sorted form

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
hrs= dict()
for line in handle :
    if not line.startswith("From") :
        continue

    lst=line.split()
    if len(lst) < 3 :
        continue

    hour=lst[5]
    hour=hour[:2]

    hrs[hour]=hrs.get(hour,0)+1

nlst = list()
for k,v in hrs.items() :
    ntup=(k,v)
    nlst.append(ntup)

nlst.sort()
for (k,v) in nlst :
    print(k,v)
