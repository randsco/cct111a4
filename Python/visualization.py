import csv

readfile = 'measles.csv' # Initialize readfile constant.
writefile = '' # Initialize writefile variable.

def get_writefile():
    '''
    UserStory1 Main Function
    
    Gets the name of the new file from the user.
    '''
    writefile = str(input('Input name of new file: '))
    while len(writefile) == 0:
        print('The name of the new file cannot be nothing.')
        writefile = str(input('Input name of new file: '))
    return writefile

def get_years():
    '''
    UserStory2 Helper Function, UserStory7 Main Function
    
    Gets the integer year 1980-2017 or "ALL" to display from the user.
    '''
    year = input('Enter a year 1980-2017 inclusive: ')
    if year.upper() == 'ALL':
        years = []
        for i in range(2017, 1980-1, -1):
            years.append(str(i))
        return years
    return [year]

def get_income():
    '''
    UserStory5 Helper Function, UserStory7 Main Function
    
    Gets the income levels to display from the user, an integer 1-4 or "ALL".
    '''
    levels = {1: 'WB_LI', 2: 'WB_LMI', 3: 'WB_UMI', 4: 'WB_HI'}
    num = input('Select 1:Low, 2:Low Middle, 3:Upper Middle, 4:High Income ')
    if num.upper() == 'ALL':
        return [levels[1], levels[2], levels[3], levels[4]]
    return levels[int(num)]

def write_rows(csv_reader, csv_writer, year_input, income_input):
    '''
    UserStory5 Helper Function
    
    Writes selected rows from measles.csv to new file.
    '''
    csv_writer.writeheader()
    for row in csv_reader:
        country_name = row['Country']
        income_level = row['World_Bank_Income_Level']
        row_buffer = {}
        if income_level in income_input:
            row_buffer['Country'] = country_name
            row_buffer['World_Bank_Income_Level'] = income_level
            for year in year_input:
                inoc_percent = row[f'{year}']
                row_buffer[f'{year}'] = inoc_percent
            csv_writer.writerow(row_buffer)    

def copy_selected(readfile, writefile):
    '''
    UserStory5 Main Function
    
    Copies years and income levels selected by user to a new file.
    '''
    with open(readfile, mode='r') as csv_file: # Open measles.csv for reading.
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        year_input = get_years() # Selects column of information.
        income_input = get_income() # Selects rows of information.
    
        with open(writefile, 'w+') as new_csv_file: # Open file named by user
                                                    # for writing, create if it
                                                    # does not exist.
            fieldnames = ['Country', 'World_Bank_Income_Level'] + year_input
            csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
            write_rows(csv_reader, csv_writer, year_input, income_input)
        new_csv_file.close()
    csv_file.close()
    
    return None

def display_reccords(file_name):
    '''
    UserStory6 Main Function
    
    Displays information about data queried by user.
    - The count of records in the input file that match the user’s criteria
    - The average percentage for those records (displayed with one fractional digit)
    - The country with the lowest percentage for those records
    - The country with the highest percentage for those records
    - The name of the country and the percent of children vaccinated will be
      displayed for the last two items (lowest percentage and highest percentage).
    '''
    with open(file_name, 'r') as values_file:
        csv_reader = csv.reader(values_file)
        
        year_count = len(next(csv_reader)[2:])-1

        record_count=0
        percentage_variable=0
        average_percentage=0

        #if income!='ALL':
            #for line in csv_reader:
                #record_count += 1
                #percentage_variable+=int(line[2])
                #average_percentage= percentage_variable/record_count

        #else:
        for num in range(year_count+1):
            values_file.seek(0)
            for line in csv_reader:
                record_count += 1
                country_name = line[0]
                if len(line[num+2]) > 0 and type(line[num+2]) is int:
                    percentage_variable += int(line[num+2])
        average_percentage = percentage_variable/record_count
        values_file.close()

        print('Total records queried:', record_count)
        print('Average inoculation rate from queried data:', average_percentage)
        print(f'The country with the lowest inoculation rate in the queried data is {lowest_country} at {lowest_rate}.')
        print(f'The country with the highest inoculation rate in the queried data is {highest_country} at {highest_rate}.')

       # for line in csv_reader:
        #    print(line[])


#the_income= get_income()

################################################################################
# MAIN PROGRAM #################################################################
################################################################################

writefile = get_writefile()
#copy_selected('measles.csv', writefile)
display_reccords(writefile)