import csv
with open ("greenhouse.csv",'r') as green:
    reader=csv.reader(green)

    with open("newGH.csv",'w') as new:
        writer=csv.writer(new)
        for data in reader:
            writer.writerow(data)
