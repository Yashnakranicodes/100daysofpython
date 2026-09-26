# 🖼️ Day 3

In day 3 I will make a simple **Expense Tracker with *json*** in which we will add some features like - 
* Adding new Expense.
* all expense.
* Total Expense with category
* deleting a Expense (which was absent feature when we were using *CSV*).

---

## Used library & built in python functions

We'll use only json, we can here use os or pathlib module for easier file management and for error mangement but I'll assume that file is in our working dir.
json make this project easy and more readable than csv and is more easy to manipulate.
json is very usefull and easy lib we will use it in future.

**code**

```py
import json

def func1(newe):
    with open("day3.json") as file :
        data = json.load(file)

    data.append(newe)

    with open("day3.json", "w") as nf :
        json.dump(data , nf, indent=1)

def func2():
    with open("day3.json") as file :
        data = json.load(file)

    for mat in data :
        print("category:", mat["category"],"type: ",mat["type"],"amount: ", mat["amount"], "date: ", mat["date"])    
    
def func3():
    with open("day3.json") as file :
        data = json.load(file)
    tta = 0
    for all in data :
        tta+=int(all["amount"])
    print(f"the totat amount is {tta}")    
    catdict = {}
    for each in data:
        if each["category"] in catdict:
            catdict[each["category"]] += int(each["amount"])
        else :
            catdict[each["category"]] = int(each["amount"])
    owlist = catdict.items()
    for _llp in owlist:
        print(
           f"{ _llp[0]} | { _llp[1]}"
        )

def func4(c , t, d):
    with open("day3.json") as file :
        data = json.load(file)
    datan = []
    for nd in data :
        if nd["category"] == c and nd["type"] == t and nd["date"] == d :
            pass
        else :
            datan.append(nd)
    with open("day3.json", "w") as le :
        data = json.dump(datan, le, indent=1)

while True:
    print(
        "|||||||||Expense Tracker|||||||||\n" \
        "1. Add a Expense\n" \
        "2. View All expenses\n" \
        "3. Total Expence by categories\n" \
        "4. Delete a expense\n" \
        "5. Exit\n"
    )
    try :
        selector = int(input("select the function : "))
    except:
       print("pls select from above 'NUMBER'")

    if selector == 1 :
        category =input("category: ").lower()
        tyype = input("type: ").lower()
        amount =input("amount: ")
        datee = input("date: ")

        thenewe = { "category": category , "type": tyype ,"amount": amount, "date":datee}

        func1(thenewe)

    elif selector == 2 :
        func2()

    elif selector == 3 :
        func3()

    elif selector == 4 :
        try:
            category =input("category: ").lower()
            tyyype = input("type: ").lower()
            datee2 = input("date of purchase: ")
            print(f"are you sure to delete the expense in {datee2} of {tyyype}!\n" \
            "if yes write YES else NO")
            confirmation = input()
            if confirmation == "YES" :
                func4(category, tyyype, datee2)
            else :
                print("ok expense is not deleted")
        except:
            print("maybe your written data is incompelte/wrong")

    elif selector == 5 :
        break

    else :
        print("its not in above function")
```

### That's it for now 

We'll try to make code more readable next time.
if there is any error in any code you can say to me.

**NOTE** -->
used concepts:
* loops
* conditionals
* json
* exceptional handling