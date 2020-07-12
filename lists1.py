#read all the content of the file and then sort all the words alphabetically

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
word = list()
for line in fh:
    lst=line.split()
    for w in lst :
        if w not in word :
            word.append(w)

word.sort()
print(word)
