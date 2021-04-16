# Author: Rachit Kakkar
# Description: Get Useful Data From Dataset
import csv
with open('sample.csv', newline='') as csvfile:
    customerdata = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in customerdata:
        try:
            if 'True' in row[0]:
                print(row)
        except:
            print(row)
