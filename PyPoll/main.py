

# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Resource         
tot_votes = 0
candidates = []
candidates_votes = {}

load_data = "Resources/election_data.csv"  
with open(load_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)
# Set up total vote counter
   

# Loop through
    for row in csv_reader:
        tot_votes += 1
        name = row[2]
        if name not in candidates:
            candidates.append(name)
            candidates_votes[name] = 0
           

        
        candidates_votes[name] += 1

#print(tot_votes) 
#print(candidates_votes) 

# percentage
percentage = {key: round(val / tot_votes *100, 3) for key,val in candidates_votes.items()}      
#print(percentage) 
max_value = max(candidates_votes, key=candidates_votes.get)
#print(max_value) 

write_data = "analysis/election_analysis.txt"  
with open(write_data, 'w') as text_file:



    output_1 = (
    f'Election Results\n'
    f'-------------------------\n'
    f'Total Votes: {tot_votes}\n'
    f'-------------------------\n'
    )
    print(output_1)
    text_file.write(output_1)

    for k, v in candidates_votes.items():

        output_2 = (f'{k}: {percentage[k]}% ({v})\n')
        print(output_2)
        text_file.write(output_2)
    output_3 = (
    f'-------------------------\n'
    f'Winner: {max_value}\n'
    f'-------------------------'
    )
    print(output_3)
    text_file.write(output_3)