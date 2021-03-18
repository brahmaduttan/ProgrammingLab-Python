import csv
with open( 'leauge.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Jersry No", "Player name----->", "Club"])
    writer.writerow([7, "Cristiano Ronaldo--->", "Real Madrid F C"])
    writer.writerow([10, "Lionel Messi----->", "F C Barcelona"])


with open('leauge.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1]+" "+row[2])
