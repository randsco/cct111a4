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



def display_reccords(file_name, income):
    with open(file_name, 'r') as values_file:
        csv_reader = csv.reader(values_file)

        next(csv_reader)

        record_count=0
        percentage_variable=0
        average_percentage=0

        if income!='ALL':
            for line in csv_reader:
                record_count += 1
                percentage_variable+=int(line[2])
                average_percentage= percentage_variable/record_count

        else:
            for num in range(37):
            
                for line in csv_reader:
                    print(num)
                    record_count +=1
                    percentage_variable+=int(line[num+2])
                    average_percentage= percentage_variable/record_count
                

        print(record_count)
        print(percentage_variable)
        print(average_percentage)

       # for line in csv_reader:
        #    print(line[])


#the_income= get_income()

display_reccords(readfile,'ALL')

