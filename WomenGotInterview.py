import csv
from datetime import datetime
import matplotlib as mpl

def convert_unix_time_to_date(unix_time_seconds):
    # Convert Unix time to a datetime object
    date_object = datetime.utcfromtimestamp(unix_time_seconds)
    # print(type(date_object))

    # Format the datetime object as a string
    formatted_date = date_object.strftime("%Y-%m")

    return formatted_date

with open('Data.csv', encoding='utf8', newline='') as datafile:
    datareader = csv.reader(datafile, dialect='excel')
    header_row = datareader.__next__()

    date_of_posting = header_row.index("date_of_posting")
    FemaleFlag = header_row.index("FemaleFlag")
    CalLetterFlag = header_row.index("CalLetterFlag")

    oldest_date = 0
    latest_date = 0

    womenInvitedToInterview = 0;
    lawImplementationDate = '2018-04'
    totalNumApplicants = 0;
    totalNumInvitedToInterview = 0
    percentage = 0
    x = []
    y = []
    for row in datareader:
        date = convert_unix_time_to_date(int(row[date_of_posting]))
        femaleFlag = int(row[FemaleFlag])
        calLetterFlag = int(row[CalLetterFlag])

        #Total Number of people who applied (M & F)
        totalNumApplicants += 1;

        #Total number of people invited to an interview
        if (calLetterFlag == 1):
            totalNumInvitedToInterview += 1;
        #percentage of women who are invited to an interview

        #Number of Female applicants who are invited to an interview
        if ((calLetterFlag) == 1 and (femaleFlag == 1)):
            womenInvitedToInterview += 1
            percentage = (womenInvitedToInterview / totalNumInvitedToInterview) * 100
            percentage = round(percentage,2)
        #percentage

        if(date < lawImplementationDate):
            x.append(date)
            y.append(percentage)
            print(date)
            print(femaleFlag)
            print(calLetterFlag)
            print('percentage of women who got an interview: ', percentage, '%')
            print('Total Num Applicants: ',totalNumApplicants)
            print('Total Num interview: ', totalNumInvitedToInterview)
            print()


    mpl.plot(x,y)
    mpl.show()