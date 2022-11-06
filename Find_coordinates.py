import csv
from astroquery.simbad import Simbad

file = open('to_add_coordinates.csv')

filereader = csv.reader(file)
header = []
header = next(filereader)
print(header)
ra_index = header.index('RA')
dec_index = header.index('dec')
rows = []
for row in filereader:
    object_name = row[0]
    print(row[0])
    try:
        result_table = Simbad.query_object(object_name)
        RA = result_table['RA'].value[0]
        dec = result_table['DEC'].value[0]
        row[ra_index] = RA
        row[dec_index] = dec
        rows.append(row)        
    except Exception as e:
        print(e)

with open('coordinates_added.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
    
