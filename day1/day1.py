import csv
while True :
    print("||||||||||||||||||||||||student manager||||||||||||||||||||||||\n"
        "want to add new student    (press 1 & Enter)\n"
        "want to knew about student (press 2 & Enter)\n" 
        "want a statistics          (press 3 & Enter)\n"
        "end the programme          (press 4 & Enter)"
    )

    try:
        firstinp = int(input("which fuction: "))
    except:
        print("wrong selection or typed str")

    else:
        if firstinp == 1 :
            print("adding a name-----")
            name = input("enter the name: ")
            rollno = input("roll number: ")
            age = input("age of student: ")
            sub = input("subject: ")
            marks = input("what are the marks: ")

            with open("day1.csv", "a", newline="") as stu :
                fields = ["name", "rollno", "age", "subject", "marks"]
                dic_writer = csv.DictWriter(stu , fieldnames=fields)

                dic_writer.writerow({"name":f"{name}", "rollno":f"{rollno}", "age":f"{age}", "subject":f"{sub}", "marks":f"{marks}"})

        elif firstinp ==2 :
            print("search the details-------")
            student = input("enter the name of student which you need to find the details of: ")
            with open("day1.csv", "r") as details :
                reading = csv.DictReader(details)
                for stu in reading:
                    if stu["name"] == student :
                        print(f"roll number : {stu["rollno"]}\n"
                            f"name  : {stu["name"]}\n"
                            f"age   : {stu["age"]}\n"
                            f"sub   : {stu["subject"]}\n"
                            f"marks : {stu["marks"]}")
                
        elif firstinp == 3:
            print(
                "---------------------------------------------\n"
                "For higest and lowest marks (press 1 & Enter)\n" 
                "For average marks           (press 2 & Enter)\n" 
                "For top 3                   (press 3 & Enter)\n"
            )
            try:
                num = int(input("Select from the following: "))
            except:
                print("wrong selection or typo misktake")
                
            if num ==1 :#h-l
                with open("day1.csv", "r") as high:
                    read = csv.DictReader(high)
                    ranks = []
                    for stu in read :
                        ranks.append(stu)
                    sorted_ranks = sorted(ranks , key= lambda x : x["marks"], reverse=True)
                    print(
                        f"The top student is {sorted_ranks[0]["name"]} with {sorted_ranks[0]["marks"]} marks \n"
                        f"The weakest student is {sorted_ranks[-1]["name"]} with {sorted_ranks[-1]["marks"]} marks"
                    )

            elif num==2 :#avg
                with open("day1.csv", "r") as high:
                    read = csv.DictReader(high)
                    avg = []
                    for stu in read :
                        avg.append(stu)
                    deno = len(avg)
                    numer = 0
                    for mark in avg :
                        each_marks = int(mark["marks"])
                        numer+=each_marks
                    the_avg = numer/deno
                    print(f"The avg marks of the class is {the_avg}")
                
            elif num==3:#top3
                with open("day1.csv", "r") as high:
                    read = csv.DictReader(high)
                    ranks = []
                    for stu in read :
                        ranks.append(stu)
                    sorted_ranks = sorted(ranks , key= lambda x : x["marks"], reverse=True)
                    top3 = sorted_ranks[:3]
                    rak = 1
                    for t3 in top3:
                        print(f"{t3["name"]} is {rak} with {t3["marks"]}")
                        rak += 1

        elif firstinp == 4:
            print("Thankyou, programme ended")
            break