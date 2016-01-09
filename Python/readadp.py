# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:36:50 2016

@author: Dino
"""

# TODO: figure out how to get automatically get file NAME from
# AppleScript into Python as a variable, during folder action.


import re
import csv

# wd_path = '{}/'.format(os.getcwd())

infile_name = 'testfile_dec8_dec12'
infile_path = '{}.csv'.format(infile_name)

# infile_path = '{}{}.csv'.format(wd_path, infile_name)

outfile_name = infile_name + '_OUT'
outfile_path = '{}.csv'.format(outfile_name)


csv_dict = []

with open(infile_path, "r") as source:
    rdr = csv.DictReader(source)
    for line in rdr:
        csv_dict.append(line)

# Fix empty fields (consecutive commas issue).
for line in csv_dict:
    for k, v in iter(line.items()):
        if v == '':
            line[k] = 'NA'
ln = []

# Fix last name error.
for line in csv_dict:
    last_name = line['Last Name']
    ln.append(re.search(r"(\w+)(,)(\W)(\w+)(\W+)", last_name).group(1))


"""
    with open('result','w') as result:
        wtr= csv.writer(result)
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[3], r[4]) )
            """
# print(wd_path)
