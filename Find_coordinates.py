import csv
from astroquery.simbad import Simbad

def find_coordinates(object_name):
    '''
    Parameters
    -----------------------
    object_name: str, Name of object

    Return
    -----------------------
    RA: RA of object
    dec: Declination of object
    '''
    result_table = Simbad.query_object(object_name)
    RA = result_table['RA'].value[0]
    dec = result_table['DEC'].value[0]
    return RA, dec

def adding_coordinates_to_file(file_name):
    '''
    Parameters
    -----------------------
    file_name: path and name of csv file. First column should be the object name. Add blank columns with titles 'RA' and 'dec'

    Return
    -----------------------
    A new csv file with the coordinates of stars. File name will be 'coordinates_added.csv' and saved in the directory of this code.
    '''
    file = open(file_name)
    filereader = csv.reader(file)
    header = []
    header = next(filereader)
    ra_index = header.index('RA')
    dec_index = header.index('dec')
    rows = []
    for row in filereader:
        object_name = row[0]
        print(row[0])
        try:
            RA, dec = find_coordinates(object_name)
            row[ra_index] = RA
            row[dec_index] = dec
            rows.append(row)        
        except Exception as e:
            print(e)

    with open('coordinates_added.csv', 'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print('Your file had been saved in the name coordinates_added.csv.')

file_name = input('Enter the path and name of csv file:')
adding_coordinates_to_file(file_name)
