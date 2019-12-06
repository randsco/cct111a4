import csv

readfile = 'measles.csv'
writefile = ''

def get_year():
    year = input('Enter a year 1980-2017 inclusive: ')
    while(1980 >= year >= 2017):
        print('Must be a year between 1980 and 2017 inclusive.')
        year = input('Enter a year 1980-2017 inclusive: ')
        if year.upper() == 'ALL':
            return 'ALL'
    if year.upper() == 'ALL':
        return 'ALL'
    return year

def get_income():
    levels = {1: 'WB_LI', 2: 'WB_LMI', 3: 'WB_UMI', 4: 'WB_HI'}
    income = input('Select 1:Low, 2:Low Middle, 3:Upper Middle, 4:High Income ')
    while(income not in levels):
        print('Must be a number 1-4.')
        income = input('Select 1:Low, 2:Low Middle, 3:Upper Middle, 4:High Income ')
        if income.upper() == 'ALL':
            return 'ALL'
    if income.upper() == 'ALL':
        return 'ALL'
    return income

def copy_selected(readfile, writefile):
    with open(readfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        year = get_year() # Selects column of information
        income = get_income() # Selects rows of information

