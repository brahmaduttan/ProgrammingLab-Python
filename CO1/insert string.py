word = input("Type First Word : ")
word2 = input("Type Second Word : ")
position = int(input("Enter insert postion : "))
result = word[:position]+word2+word[position:]
print(result)