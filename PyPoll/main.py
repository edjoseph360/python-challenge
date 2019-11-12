import os
import csv

csvpath = "election_data.csv"
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    data = []
    for row in csvread:
        data.append(row)
        
 
    max_len_of_rows = len(data)


    print("Election Results")
    print("Total Votes:",max_len_of_rows)


    Khanvotes=0
    Correyvotes=0
    Livotes=0
    Otooleyvotes=0


    for i in range(max_len_of_rows):
        if data[i][2]=="Khan":
            Khanvotes=Khanvotes+1

        if data[i][2]=="Correy":
            Correyvotes=Correyvotes+1

        if data[i][2]=="Li":
            Livotes=Livotes+1

        if data[i][2]=="O'Tooley": 
            Otooleyvotes=Otooleyvotes+1


khanpercent=Khanvotes/max_len_of_rows*100
Correypercent=Correyvotes/max_len_of_rows*100
lipercent=Livotes/max_len_of_rows*100
otoolypercent=Otooleyvotes/max_len_of_rows*100


print("Khan:", int(khanpercent),"%", Khanvotes)
print("Correy:", int(Correypercent),"%", Correyvotes)
print("Li:", int(lipercent),"%", Livotes)
print("O'Tooley:", int(otoolypercent),"%", Otooleyvotes)
            
