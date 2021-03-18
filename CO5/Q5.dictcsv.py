import csv

f = open("fruits.csv","w",newline='')
writer = csv.DictWriter(f, fieldnames = ["fruit","count"])
writer.writeheader()
writer.writerow({"fruit":"Orange", "count": "10"})
writer.writerow({"fruit": "Grapes", "count": "22"})
f.close()
c = 0
f = open("fruits.csv")
reader = csv.DictReader(f)
# for row in reader:
    # print(row)
for row in reader:
    if c==0:
        print(f'{"".join(row)}')
        c+=1
    print(f'{row["fruit"]},{row["count"]}')
    c+=1
print(c-1)
f.close()
