import json
import csv
from traceback import print_list


# Opening JSON file and loading the data
# into the variable data
with open('info.json') as json_file:
    data = json.load(json_file)

employee_data = data['result']['hits']['hit']

# now we will open a file for writing
data_file = open('info.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0
for emp in employee_data:
    rec = emp['info']
    row = {"authors": "","title": "","venue": "","volume": "","number": "","pages": "","year": "","type": "",
            "access": "","key": "","doi": "","ee": "","url": ""}
    if count == 0:
        # Writing headers of CSV file
        header = row.keys()
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
    row['authors'] = authors
    if 'title' in rec.keys():
        row['title'] = rec['title']
    if 'venue' in rec.keys():
        row['venue'] = rec['venue']
    if 'volume' in rec.keys():
        row['volume'] = rec['volume']
    if 'number' in rec.keys():
        row['number'] = rec['number']
    if 'pages' in rec.keys():
        row['pages'] = rec['pages']
    if 'year' in rec.keys():
        row['year'] = rec['year']
    if 'type' in rec.keys():
        row['type'] = rec['type']
    if 'access' in rec.keys():
        row['access'] = rec['access']
    if 'key' in rec.keys():
        row['key'] = rec['key']
    if 'doi' in rec.keys():
        row['doi'] = rec['doi']
    if 'ee' in rec.keys():
        row['ee'] = rec['ee']
    if 'url' in rec.keys():
        row['url'] = rec['url']
    csv_writer.writerow(row.values())
data_file.close()