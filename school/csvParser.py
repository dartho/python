import csv

csvfile = open("data/input1.csv")
reader = csv.reader(csvfile, delimiter=",")
unique = {}
for row in reader:
    for key in row:
        if key in unique:
            unique.update({key: unique[key] + 1})
        else:
            unique.update({key: 1})

for key in unique:
    print(key, "-", unique[key])
