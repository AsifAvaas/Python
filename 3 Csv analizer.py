import csv

def readFile(csvfile):
    with open(csvfile,"r") as file:
        reader=csv.reader(file)
        for line in reader:
            if len(line)<3:
                continue
            print(f"{line[0]} {line[1]} {line[2]}")
        print("\n")


def writeFile(csvfile):
    with open(csvfile,'a',newline='') as file:
        writer=csv.writer(file)
        cat=input("Enter the category: ")
        sales=input("Enter the sales: ")
        date=input("Enter the date: ")
        writer.writerow([cat,sales,date])
        print('\n')
        

def calculateSum(csvfile):
    with open(csvfile,'r') as file:
        reader=csv.reader(file)
        sum=0
        next(reader)
        for line in reader:
            sum+=int(line[1])
        print('\n')
        return sum
    

def calculateAvg(csvfile):
    with open(csvfile,'r') as file:
        reader=csv.reader(file)
        sum=0
        n=0
        next(reader)
        for line in reader:
            sum+=int(line[1])
            n+=1
        print('\n')
        return sum/n


csv_file="sales.csv"
while True:
    print("Press 1 to read the file: ")
    print("Press 2 to write something in the file: ")
    print("Press 3 to calculate the sum of sales: ")
    print("Press 4 to calculate the average of sales: ")
    print("Press other to close the file: ")
    choice=int(input("Enter: "))

    if choice==1:
        readFile(csv_file)
    elif choice==2:
        writeFile(csv_file)
    elif choice==3:
        print(f"sum is ={calculateSum(csv_file)}")
        print("\n")
    elif choice==4:
        print(f"Average is ={calculateAvg(csv_file)}")
        print("\n")
    else:
        print("Tank You")
        break