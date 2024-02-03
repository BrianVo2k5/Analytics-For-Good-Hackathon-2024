import csv
import calendar
import time

with open('Data.csv', encoding='utf8', newline='') as datafile:
    company = set()
    data_availability_income = set()
    data_availability_revenue = set()
    datareader = csv.reader(datafile, dialect='excel')
    header_row = datareader.__next__()
    print(header_row)

    client_id = header_row.index("client_id")
    Net_Income = header_row.index("NetIncome")
    Revenue = header_row.index("OperatingRevenue")

    apiApplicationsCreated = header_row.index("api_applications_created")

    lawImplementationTime = calendar.timegm(time.strptime("Apr 1 2017", "%b %d %Y"))

    # 1 year, for now
    timeInterval = 60 * 60 * 24 * 365



    for row in datareader:
        appCreated = int(row[apiApplicationsCreated])

        if lawImplementationTime - timeInterval <= appCreated < lawImplementationTime:
            company.add(row[client_id])
            data_availability_income.add(row[Net_Income])
            data_availability_revenue.add(row[Revenue])


print(f"number of companies: {len(company)}")
print(f"number of available data (Net Income): {len(data_availability_income)}")
print(f"number of available data (Revenue): {len(data_availability_revenue)}")
