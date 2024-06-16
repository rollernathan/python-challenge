# Import the os module
import os

# Import module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# I believe there is a way to do this using dictionaries, but I was struggling to figure that out, so I went with lists instead.
# Please provide how to do with dictionaries so I can learn that method as well, since it is probably clearer and more efficient.

# Create variables to store the total votes, winner votes, and winner and lists to store the election data and unique candidate data
total_votes = 0
ballot_ID = []
county = []
candidate = []
unique_candidates = []
unique_candidates_votes = []
unique_candidates_percent = []
winner_votes = 0
winner = 'no one'

# Read using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header and store in lists
    for row in csvreader:
        ballot_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        # Count the total number of votes
        total_votes +=1

        # Populate the list of the unique candidates
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])

# Calculate the number of votes for each candidate
for i in range(len(unique_candidates)):
    unique_candidates_votes.append(0)
    for x in candidate:
        if x == unique_candidates[i]:
            unique_candidates_votes[i] +=1

# Calculate the percent of votes for each candidate
for i in range(len(unique_candidates)):
    unique_candidates_percent.append(round(100*unique_candidates_votes[i]/total_votes,3))

# Idnetify and store the winner
for i in range(len(unique_candidates_votes)):
    if unique_candidates_votes[i] > winner_votes:
        winner_votes = unique_candidates_votes[i]
        winner = unique_candidates[i]

# Print all of the results as required in the challenge
print('\nElection Results\n')
print('-------------------------\n')
print(f'Total Votes : {total_votes} \n')
print('-------------------------\n')
for i in range(len(unique_candidates)):
    print(f'{unique_candidates[i]}: {unique_candidates_percent[i]}% ({unique_candidates_votes[i]})\n')
print('-------------------------\n')
print(f'Winner: {winner}\n')
print('-------------------------\n')

# Specify the file to write to
output_path = os.path.join('analysis', 'election_results.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:

    # Write the print statements to the file
    file.write('\nElection Results\n')
    file.write('-------------------------\n')
    file.write(f'Total Votes : {total_votes} \n')
    file.write('-------------------------\n')
    for i in range(len(unique_candidates)):
        file.write(f'{unique_candidates[i]}: {unique_candidates_percent[i]}% ({unique_candidates_votes[i]})\n')
    file.write('-------------------------\n')
    file.write(f'Winner: {winner}\n')
    file.write('-------------------------\n')
    file.close()

# Notify the user the results have been written to the output file.
print("Election Results have been written to 'analysis\\election_results.txt'.\n")