import csv

with open('Data.csv', encoding='utf8', newline='') as datafile:
    women = 0
    datareader = csv.reader(datafile, dialect='excel')
    header_row = datareader.__next__()
    print(header_row)

    femaleFlag = header_row.index("FemaleFlag")

    for row in datareader:
        if row[femaleFlag] == '1':
            women += 1

print(women)
