# Author: Rachit Kakkar
# Description: Get Useful Data From Dataset
import csv
from better_profanity import profanity
csv.field_size_limit(1000000000)

ocurrences = 0
with open('twcs.csv', errors='ignore') as csvfile:
    customerdata = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in customerdata:
        try:
            if 'True' in row[0]:
                    line = ''

                    for i in range(1, len(row)):
                        line = line + ' ' + row[i]

                    if 'VerizonSupport' in line:
                        if not profanity.contains_profanity(line):
                            #print('   ')
                            ocurrences += 1
                            #print(line)
        except:
            pass

print(ocurrences)
