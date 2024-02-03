import csv
import calendar
import time

with open('Data.csv', encoding='utf8', newline='') as datafile:
    womenBefore = 0
    womenAfter = 0
    nonWomenBefore = 0
    nonWomenAfter = 0
    datareader = csv.reader(datafile, dialect='excel')
    header_row = datareader.__next__()
    print(header_row)

    lawImplementationTime = calendar.timegm(time.strptime("Apr 1 2017", "%b %d %Y"))

    # 1 year, for now
    timeInterval = 60*60*24*365

    femaleFlag = header_row.index("FemaleFlag")
    apiApplicationsCreated = header_row.index("api_applications_created")

    for row in datareader:
        appCreated = int(row[apiApplicationsCreated])
    
        if lawImplementationTime - timeInterval <= appCreated < lawImplementationTime:   
            if row[femaleFlag] == '1':
                womenBefore += 1
            else:
                nonWomenBefore += 1
        
        elif lawImplementationTime <= appCreated <= lawImplementationTime + timeInterval:
            if row[femaleFlag] == '1':
                womenAfter += 1
            else:
                nonWomenAfter += 1

print(womenBefore)
print(womenAfter)
print(nonWomenBefore)
print(nonWomenAfter)

print("Women had a " + str(100 * (womenAfter-womenBefore)/womenBefore) + "% increase")
print("Non-Women had a " + str(100 * (nonWomenAfter-nonWomenBefore)/nonWomenBefore) + "% increase")