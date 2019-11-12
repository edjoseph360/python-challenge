import os
import csv
#csvpath = os.path.join("CU-NYC-DATA-PT-10-2019-U-C" , "Homework", "03-Python", "Instructions", "PyBank", "Resources","budget_data")
#csvpath = "\Users\edste\CU-NYC-DATA-PT-10-2019-U-C\Homework\03-Python\Instructions\PyBank\budget_data.csv"
csvpath = "budget_data.csv"
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    data = []
    for row in csvread:
        data.append(row)
        
 
    print(data)
    max_len_of_rows = len(data)

    total = 0
    for i in range(max_len_of_rows):
        total=total+int(data[i][1])

    biggest_increase = 0
    biggest_increase_month = ""
    biggest_decrease = 0
    biggest_decrease_month = ""
    CHANGE=[]
    for j in range(1,max_len_of_rows):
        Montly_change=int(data[j][1]) - int(data[j-1][1])
        CHANGE.append(Montly_change)

        if Montly_change > biggest_increase:
            biggest_increase=Montly_change
            biggest_increase_month=data[j][0]


        if Montly_change < biggest_decrease:
            biggest_decrease=Montly_change
            biggest_decrease_month=data[j][0]



    Average_Change = sum(CHANGE)/len(CHANGE)


    print("Financial Analysis")
    print("Total:", total)
    print("Average Change:", Average_Change)
    print("Total Months:", max_len_of_rows)
    print("Biggest Increase:", biggest_increase,biggest_increase_month)
    print("Biggest Decrease:", biggest_decrease,biggest_decrease_month)




 