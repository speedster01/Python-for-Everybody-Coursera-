# Use words.txt as the file name
#read all content in file then covert it into upper case
fname = input("Enter file name: ")
try:
    fh = open(fname)
except :
	print("Entered file not found")

for txt in fh :
    txt=txt.rstrip()
    txt=txt.upper()
    print(txt)
