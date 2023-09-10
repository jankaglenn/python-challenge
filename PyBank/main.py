
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
from datetime import date

text_output = ""
def load_data(budget_data):
    mylist = []
    with open(budget_data) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        diff = 0
        tot_diff = 0
        net = 0
        prev = 0
        greatest_increase = 0
        greatest_increase_month = ''
        greatest_decrease = 0
        greatest_decrease_month = ''
        # We count total months
        for row in csv_reader:
            profit_loss = int(row['Profit/Losses'])
            net = net + profit_loss
            diff = profit_loss - prev
            prev = profit_loss
            
            if diff > greatest_increase:
                greatest_increase = diff
                greatest_increase_month = row['Date']

            if diff < greatest_decrease:
                greatest_decrease = diff
                greatest_decrease_month = row['Date'] 
            
            if len(mylist) > 0:
                tot_diff = tot_diff + diff

            mylist.append(row)

    average_change = round(tot_diff / (len(mylist) -1), 2)
    
    text_output = ('Financial Analysis\n'
    
    f'------------------------\n'

    f'Months {len(mylist)}\n' 
    f'Net Profit/Loss: {net}\n'
    f'Avg. Change: {average_change}\n'
    f'Greatest Increase: {greatest_increase_month}  ${greatest_increase}\n'
    f'Greatest Decrease: {greatest_decrease_month}  ${greatest_decrease}')
    
    return(text_output)
#Resource         
text_out = load_data("Resources\\budget_data.csv")
print(text_out)
output_file = "analysis/budget_analysis.txt"
with open(output_file, "w") as textfile:
   textfile.write(text_out)
