import csv
import calendar
import time

with open('Data.csv', encoding='utf8', newline='') as datafile:

    womenBefore_grad = 0
    womenBefore_grad_cv_completion = 0

    womenBefore_postgrad = 0
    womenBefore_postgrad_cv_completion = 0

    womenAfter_grad = 0
    womenAfter_grad_cv_completion = 0

    womenAfter_postgrad = 0
    womenAfter_postgrad_cv_completion = 0

    datareader = csv.reader(datafile, dialect='excel')
    header_row = datareader.__next__()
    #print(header_row)

    lawImplementationTime = calendar.timegm(time.strptime("Apr 1 2017", "%b %d %Y"))

    # 1 year, for now
    timeInterval = 60 * 60 * 24 * 365

    femaleFlag = header_row.index("FemaleFlag")
    apiApplicationsCreated = header_row.index("api_applications_created")
    CourseType = header_row.index("course_type")
    CV_Completion = header_row.index("profile_percentage")

    for row in datareader:
        appCreated = int(row[apiApplicationsCreated])

        if lawImplementationTime - timeInterval <= appCreated < lawImplementationTime:
            if row[femaleFlag] == '0':
                if row[CourseType] == 'pg':
                    womenBefore_postgrad += 1
                    womenBefore_postgrad_cv_completion += int(row[CV_Completion])
                else:
                    womenBefore_grad += 1
                    womenBefore_grad_cv_completion += int(row[CV_Completion])

        elif lawImplementationTime <= appCreated <= lawImplementationTime + timeInterval:
            if row[femaleFlag] == '0':
                if row[CourseType] == 'pg':
                    womenAfter_postgrad += 1
                    womenAfter_postgrad_cv_completion += int(row[CV_Completion])
                else:
                    womenAfter_grad += 1
                    womenAfter_grad_cv_completion += int(row[CV_Completion])

print(f"Before law, women graduate count is {womenBefore_grad} and their profile completion rate (in average) is {womenBefore_grad_cv_completion / womenBefore_grad :.2f}%")
print(f"Before law, women postgraduate count is {womenBefore_postgrad} and their profile completion rate (in average) is {womenBefore_postgrad_cv_completion / womenBefore_postgrad :.2f}%")
print()
print(f"After law, women graduate count is {womenAfter_grad} and their profile completion rate (in average) is {womenAfter_grad_cv_completion / womenAfter_grad :.2f}%")
print(f"After law, women postgraduate count is {womenAfter_postgrad} and their profile completion rate (in average) is {womenAfter_postgrad_cv_completion / womenAfter_postgrad :.2f}%")
