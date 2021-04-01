# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

# define variables
months = []
profit_loss_changes = []
total_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# directory path
dirname = os.path.dirname(__file__)
budget_data = os.path.join(dirname, 'Resources', 'budget_data.csv')

# open budget_data.csv file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row first
    csv_header = next(csvreader)

    # Loop through all rows
    for row in csvreader:

        # The total number of months included in the dataset
        total_months = total_months +1

        # The net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (total_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
           
        else:

            # change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month 
            months.append(row[0])

            # Append each profit_loss_change 
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    # sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(total_months - 1), 2)

 
    highest_change = max(profit_loss_changes) # return largest value
    lowest_change = min(profit_loss_changes) # return smallest value

   
    highest_month_index = profit_loss_changes.index(highest_change) # use the index to call the highest month
    lowest_month_index = profit_loss_changes.index(lowest_change)   # use the index to call the lowest month
    
    # what is the best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

with open('PyBank_results', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${net_profit_loss}\n")
    text.write(f"Average Change: ${average_profit_loss}\n")
    text.write(f"Greatest Increase in Profits: {best_month} (${highest_change})\n")
    text.write(f"Greatest Decrease in Profits: {worst_month} (${lowest_change})\n")