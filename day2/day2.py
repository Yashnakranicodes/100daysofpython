import csv 

def func1():
    day = int(input("day of purchase: "))
    month = int(input("month: "))
    year = int(input("year: "))
    category = input("which category: ")
    description = input("which product: ")
    amount = int(input("the price of good: "))

    with open("day2.csv", "a", newline="") as d2:
        fields = ['date','category','desricption','amount']
        dict_writer = csv.DictWriter(d2, fieldnames=fields)

        dict_writer.writerow({"date":f"{day}-{month}-{year}","category":f"{category}","desricption":f"{description}","amount":f"{amount}"})

def func2():
    with open("day2.csv", "r") as d2 :
        reader = csv.DictReader(d2)
        print(f"Date\t\tCategory\tDesccription\tAmount")
        
        for row in reader:
            print(f"{row['date']:<15}{row['category']:<15}{row['description']:<15}{row['amount']:<15}")


def func3():
    catein = input("write the category for search: ")
    with open("day2.csv", "r") as d2:
        read= csv.DictReader(d2)
        for rows in read:
            if rows['category'] == catein :
                print(
                    f"date : {rows['date']}\n"
                    f"category : {rows['category']}"
                    f" | description : {rows['description']}"
                    f" | amount : {rows['amount']}\n"
                    "________________________\n"
                )

def func4():
    with open("day2.csv", "r") as d2:
        read= csv.DictReader(d2)
        amount = 0
        for all in read:
            amount+= int(all["amount"])
        print(f"Total Expence : {amount}\n")

while True:
    print(
        "====EXPENCE TRACKER====\n"
        "1. Add expence\n"
        "2. View expences\n" 
        "3. Search Expences\n"
        "4. Calculate total\n"
        "5. Exit"
    )

    try :
        funcinput = int(input("select from following: "))
    except:
        print("not an int or may be wrong selection")

    if funcinput > 5 :
        print("ERROR : pls select from the following")

    elif funcinput ==1 :
        func1()

    elif funcinput ==2 :
        func2()

    elif funcinput ==3 :
        func3()

    elif funcinput ==4 :
        func4()

    elif funcinput ==5 :
        print(" Exited from Expence Tracker ")
        break