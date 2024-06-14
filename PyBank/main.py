# Import the os module
import os

# Import module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Read using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

    # Create variables to store count of rows (months) and sum of profits
    # Create lists to store months and profits (could have done with dictionaries)
    count = 0
    sum = 0
    months = []
    profits = []

    # Create a list to store the change from month to month and store 0 as the change for the first month
    # Create a variable to store the sum of the changes from month to month
    change_value = [0]
    change = 0

    # Create variables to store the greatest increase and the index of the month the greatest increase occurs in
    greatest_increase = 0
    greatest_increase_index = 0

    # Create variables to store the greatest decrease and the index of the month the greatest decrease occurs in
    greatest_decrease = 0
    greatest_decrease_index = 0

    # Count months included in the data and sum the profits for all the months
    for row in csvreader:
        count += 1
        sum = sum + int(row[1])
        months.append(row[0])
        profits.append(row[1])

    # Populate the list of the change in profits from month to month
    for i in range(len(profits)-1):
        change_value.append(int(profits[i+1])-int(profits[i]))

    # Sum all the changes in profits from month to month
    for j in change_value:
        change += j
    
    # Calculate the average change in profits from month to month (divide by one less than months because there is one less
    # change than the number of months (first month has no change))
    average = round(change/(count-1),2)

    # Create variables to store the greatest increase in profits and greatest decrease in profits and assign them
    # to the change in profits from the first month
    greatest_increase = change_value[0]
    greatest_decrease = change_value[0]

    # Check each change in profits to determine if it is greater than the greatest increase (if)
    # or less than the greatest decrease (elif). If it is either of these,
    # assign the appropriate variable to store that change and the index to store the index to later reference the appropriate month
    for i in range(len(change_value)):
        if(change_value[i]>greatest_increase):
            greatest_increase = change_value[i]
            greatest_increase_index = i
            
        elif(change_value[i]<greatest_decrease):
            greatest_decrease = change_value[i]
            greatest_decrease_index = i

    # Print all of the results as required in the challenge
    print('\nFinancial Analysis\n')
    print('-----------------------------\n')
    print(f'Total Months: {count}\n')
    print(f'Total: ${sum}\n')
    print(f'Average Change: ${average}\n')
    print(f'Greatest Increase in Profits: {months[greatest_increase_index]} (${greatest_increase})\n')
    print(f'Greatest Decrease in Profits: {months[greatest_decrease_index]} (${greatest_decrease})\n')

# Specify the file to write to
output_path = os.path.join('Output', 'budget_data.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:

    # Write the print statements to the file
    file.write('\nFinancial Analysis\n')
    file.write('-----------------------------\n')
    file.write(f'Total Months: {count}\n')
    file.write(f'Total: ${sum}\n')
    file.write(f'Average Change: ${average}\n')
    file.write(f'Greatest Increase in Profits: {months[greatest_increase_index]} (${greatest_increase})\n')
    file.write(f'Greatest Decrease in Profits: {months[greatest_decrease_index]} (${greatest_decrease})\n')
    file.close()

# Notify the user the results have been written to the output file.
print("Financial Analysis Results have been written to 'Output\\budget_data.txt'.\n")