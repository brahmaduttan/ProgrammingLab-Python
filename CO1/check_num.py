num = int(input("Length of the list : "))

array = []

for n in range(num):
    new = int(input("Insert number : "))
    array.append(new)


search = int(input("Enter Number to be searched : "))

for i in array:
    if(i==search):
        print("Number is found in List ")