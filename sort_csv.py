import sys, csv ,operator

data = csv.reader(open('src.csv'),delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
#now write the sorte result into new CSV file
with open("OldFile.csv", "wb") as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)

data = csv.reader(open('tgt.csv'),delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
#now write the sorte result into new CSV file
with open("NewFile.csv", "wb") as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)


column_names = ['id','name','amount']
source_data = csv.reader(open('OldFile.csv'))
target_data = csv.reader(open('NewFile.csv'))
counter = 1
def rowElementCompare(sourceRow, targetRow):
    row_length = min(len(sourceRow), len(targetRow))
    for i in range(row_length):
        if sourceRow[i] != targetRow[i]:
            #print i
            yield i
    return
for source_row,target_row in zip(source_data,target_data):
    comparison_result = None
    for comparison_result in rowElementCompare(source_row, target_row): # UPDATED
        print "Mismatch in column %s Pre %s, Post %s" % (column_names[comparison_result],source_row[comparison_result], target_row[comparison_result])
    counter += 1
