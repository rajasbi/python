import re
import os

#fpaths = ['C:\Users\SHARMILLA\PycharmProjects\R_D\recon','C:\Users\SHARMILLA\PycharmProjects\R_D\vision']
prefixes = ('prebill','CEUE')
fpaths = ['recon','vision']

SearchStr = '23456'
import glob
requredFiles = []


for fpath in fpaths:
    for r, d, f in os.walk(r'C:\Users\SHARMILLA\PycharmProjects\R_D'):
        for newfile in f:
            if newfile.startswith(prefixes):
                requredFiles.append(os.path.join(r, newfile))
                print("hello")
'''
for fpath in fpaths:
    arr = os.listdir(fpath)
    #arr = os.walk(fpath)
    #print(arr)
    for eachfile in arr:

        if eachfile.startswith(prefixes):
            print(1, eachfile, prefixes)
            requredFiles.append(os.path.join(fpath, eachfile))
            print("hello")
'''
print(requredFiles)
for myfile in requredFiles:
    content_written = False
    resultfile = SearchStr+'_'+os.path.basename(myfile)
    with open(myfile) as infile, open('resultfile', 'w') as outfile:
        #print(outfile)
        copy = False
        for line in infile:
            if re.match("#Account:23456(.*)", line):
                outfile.write(line)
                copy = True
                content_written = True
            elif re.match("#Account(.*)", line):
                copy = False
            elif copy:
                outfile.write(line)
    if not content_written :
        os.remove(resultfile)
