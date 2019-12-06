import csv

readfile = 'measles.csv'
writefile = ''

def copy_selected(readfile, writefile):
    with open(readfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
