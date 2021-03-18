newFile = open("text.txt","a")
newFile.write("Python programming…! \n")
newFile.close()

readFile = open("text.txt","r")
print(readFile.readlines())
readFile.close()
