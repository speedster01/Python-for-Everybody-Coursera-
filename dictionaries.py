#print the email address of person who sent the maximum email

fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print("file not found")


dic=dict()
for line in fh :
    line.rstrip()
    if not line.startswith("From"):
        continue

    word=line.split()
    if len(word) < 3 :
        continue
    email=word[1]

    dic[email]=dic.get(email,0) + 1

maxnum=None
email=None

for k,v in dic.items() :
    if maxnum is None or v>maxnum :
        maxnum=v
        email=k

print(email,maxnum)
