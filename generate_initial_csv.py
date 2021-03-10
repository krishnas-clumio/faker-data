file_csv = open("./CSV Files/TestTable.csv", "w")
column = "Data_"
row_line = "PART_KEY,"+"ROW" + ","+ "DATA" +"\n"
file_csv.write(row_line)
part_key = 1
for row in range(1, 10000000):
    row_line = str(part_key)+","+str(row) + ","+column + str(row) +"\n"
    file_csv.write(row_line)
    if row%100000 == 0:
        part_key+=1
        print("Status", row)
file_csv.close()