print("hello World")
print("this is my first IDLE Python Program")

f = open("example.txt","r+") #always open a file first

#printing information from the file
for line in f:
    print("this is the first sentence in the text file: "+ line[0] +"\n")
    print("this is the rest of the lines: "+ line + "\n")

f.close()


#colecting information from the file
contents = ""
f = open ("example.txt","r+") # reopening file

for line in f:
    contents=contents + line #collect file contains into one string variable

f.close() # always remember to close files.

print(contents)
