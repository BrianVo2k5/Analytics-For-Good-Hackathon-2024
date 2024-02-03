import csv
import calendar
import time

with open('Data.csv', encoding='utf8', newline='') as datafile:

    Chennai_before = 0
    Chennai_after = 0

    Kolkata_before = 0
    Kolkata_after = 0

    Hyderabad_before = 0
    Hyderabad_after = 0

    NCR_before = 0
    NCR_after = 0

    Ahmedabad_before = 0
    Ahmedabad_after = 0

    Bangalore_before = 0
    Bangalore_after = 0

    MumbaiPune_before = 0
    MumbaiPune_after = 0

    datareader = csv.reader(datafile, dialect='excel')
    header_row = datareader.__next__()
    #print(header_row)

    lawImplementationTime = calendar.timegm(time.strptime("Apr 1 2017", "%b %d %Y"))

    # 1 year, for now
    timeInterval = 60 * 60 * 24 * 365

    femaleFlag = header_row.index("FemaleFlag")
    apiApplicationsCreated = header_row.index("api_applications_created")
    chennai = header_row.index("Chennai")
    kolkata = header_row.index("Kolkata")
    hyderabad = header_row.index("Hyderabad")
    ncr = header_row.index("NCR")
    ahmedabad = header_row.index("Ahmedabad")
    bangalore = header_row.index("Bangalore")
    mumbaipune = header_row.index("MumbaiPune")

    for row in datareader:
        appCreated = int(row[apiApplicationsCreated])

        if lawImplementationTime - timeInterval <= appCreated < lawImplementationTime:
            if row[femaleFlag] == '1':
                if row[chennai] == '1':
                    Chennai_before +=1
                if row[kolkata] == '1':
                    Kolkata_before += 1
                if row[hyderabad] == '1':
                    Hyderabad_before += 1
                if row[ncr] == '1':
                    NCR_before += 1
                if row[ahmedabad] == '1':
                    Ahmedabad_before += 1
                if row[bangalore] == '1':
                    Bangalore_before += 1
                if row[mumbaipune] == '1':
                    MumbaiPune_before += 1


        elif lawImplementationTime <= appCreated <= lawImplementationTime + timeInterval:
            if row[femaleFlag] == '1':
                if row[chennai] == '1':
                    Chennai_after += 1
                if row[kolkata] == '1':
                    Kolkata_after += 1
                if row[hyderabad] == '1':
                    Hyderabad_after += 1
                if row[ncr] == '1':
                    NCR_after += 1
                if row[ahmedabad] == '1':
                    Ahmedabad_after += 1
                if row[bangalore] == '1':
                    Bangalore_after += 1
                if row[mumbaipune] == '1':
                    MumbaiPune_after += 1

print(f"Chennai before law: {Chennai_before} & After law: {Chennai_after}")
print(f"Kolkata before law: {Kolkata_before} & After law: {Kolkata_after}")
print(f"Hyderabad before law: {Hyderabad_before} & After law: {Hyderabad_after}")
print(f"NCR before law: {NCR_before} & After law: {NCR_after}")
print(f"Ahmedabad before law: {Ahmedabad_before} & After law: {Ahmedabad_after}")
print(f"Bangalore before law: {Bangalore_before} & After law: {Bangalore_after}")
print(f"MumbaiPune before law: {MumbaiPune_before} & After law: {MumbaiPune_after}")
