# Count all the email address of sender
fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print("file not found")
count = 0
email=list()
for line in fh :
    line.rstrip()
    if not line.startswith("From"):
        continue
    count+=1
    word=line.split()
    if len(word) < 3 :
        continue
    email.append(word[1])
    print(word[1])
print("There were", len(email), "lines in the file with From as the first word")
