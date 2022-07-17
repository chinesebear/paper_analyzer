import json
import csv
from traceback import print_list


# Opening JSON file and loading the data
# into the variable data
with open('info.json') as json_file:
    data = json.load(json_file)

employee_data = data['result']['hits']['hit']

# now we will open a file for writing
data_file = open('info_journal.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for emp in employee_data:
    rec = emp['info']
    if rec['type'] == 'Journal Articles':
        if count == 0:
            # Writing headers of CSV file
            header = rec.keys()
            csv_writer.writerow(header)
            count += 1
        # Writing data of CSV file
        authors = ""
        #print(type(rec['authors']['author']))
        if type(rec['authors']['author']).__name__ == 'dict':
            authors = rec['authors']['author']['text']
        if type(rec['authors']['author']).__name__ == 'list':
            for au in rec['authors']['author']:
                if type(au).__name__ == 'dict':
                    authors += au['text'] + ';'
        rec['authors'] = authors
        csv_writer.writerow(rec.values())
data_file.close()