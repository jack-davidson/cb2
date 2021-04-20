# Author: Rachit Kakkar
# Description: Get Useful Data From Dataset
import csv
from better_profanity import profanity

def read_customer_support_data(filepath, company, print_data=True):
    ocurrences = 0
    with open(filepath, errors='ignore') as csvfile:
        customer_data = csv.reader(csvfile, delimiter=' ', quotechar='|')

        try:
            for info in enumerate(customer_data):
                line_num, row = info

                if len(row) != 0:
                    if 'True' in row[0]:
                            line = ''

                            for i in range(1, len(row)):
                                line = line + ' ' + row[i]

                            if company in line:
                                if not profanity.contains_profanity(line):
                                    if print_data:
                                        ocurrences += 1
                                        print(line)

        except:
            if print_data:
                print('ERROR:', line_num)
                

    if print_data: print(ocurrences)

if __name__ == '__main__':
    read_customer_support_data('twcs.csv','VerizonSupport')
