import csv
column_names = ['id','name','amount']
source_data = csv.reader(open('src.csv'))
target_data = csv.reader(open('tgt.csv'))
counter = 1
def rowElementCompare(sourceRow, targetRow):
    row_length = min(len(sourceRow), len(targetRow))
    for i in range(row_length):
        if sourceRow[i] != targetRow[i]:
            yield i 
    return 
for source_row,target_row in zip(source_data,target_data):
    comparison_result = None
    for comparison_result in rowElementCompare(source_row, target_row):
        print "Mismatch in column %s , source value %s, target value %s" % (column_names[comparison_result], source_row[comparison_result], target_row[comparison_result])
    counter += 1
