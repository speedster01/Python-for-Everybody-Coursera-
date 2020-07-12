# Use the file name mbox-short.txt as the file name
#Calculate the Average of number contained in line starting with "X-DSPAM-Confidence:"
fname = input("Enter file name: ")
fh = open(fname)
c=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    ind=line.find('0')
    num=line[ind:]
    num=float(num)
    total=total+num
    c=c+1

print("Average spam confidence:",total/c)
