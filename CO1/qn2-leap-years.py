current_year = int(input("Enter current year: "))
final_year = int(input("Enter final year: "))

if current_year < final_year:
  print ("Here is a list of leap years between " + str(current_year) + " and " + str(final_year)  + ":")
  
while current_year < final_year:  
    if current_year % 4 == 0:
        print(current_year)
    if current_year % 100 == 0 and current_year % 400 == 0:
        print(current_year)
    current_year +=1
