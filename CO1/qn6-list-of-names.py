names = []
num = input("Enter Number of Names : ")
a_count = 0

for i in range(int(num)):
    name = input("Input a name : ")
    names.append(name)

for name in names:
    count = name.count("a")
    a_count+=count

print(a_count)



