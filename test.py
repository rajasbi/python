import csv
import os 

def wrtdata(csvfile,headers,data):
    print(data)
    with open(csvfile, "a") as f:
        #writer = csv.DictWriter(f,fieldnames=headers)
        writer = csv.writer(f)
        print(os.stat(csvfile).st_size)
        if (os.stat(csvfile).st_size) == 0:
            writer.writerows(headers)
        writer.writerows(data)
            #writer.writerows(row + [0.0] for row in data)

csvfile = 'output.csv'
headers = ['NAME','ID','STATE','CUNTRY']
data = [['raj','','ap','ind']]
headers = [headers]
wrtdata(csvfile,headers,data)

