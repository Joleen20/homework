import csv
import os

budget_path = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("budget_analysis.txt")

total_months = 0
total_net = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0
total_monthly_change = 0
average_change = 0
greatest_increase_date = ""
greatest_decrease_date = ""

with open(budget_path) as budget_data:
    reader = csv.reader(budget_data)

    # Read the header row
    header = next(reader)
    print(header)

    first_row = next(reader)
    print(first_row)
    
    print(first_row[0])
    print(first_row[1])
    rev = int(first_row[1])
    total_net = total_net + rev
    previous_rev = rev
    print(total_net)

    total_months = total_months + 1
    print(total_months)

    for row in reader:
        total_months = total_months + 1
        print(total_months)
        print(row)
        current_rev = int(row[1])
        #print(current_rev)
        total_net = total_net + current_rev
        monthly_change= current_rev - previous_rev
        print(monthly_change)
        total_monthly_change = total_monthly_change + monthly_change
        print(total_monthly_change)
        
        if monthly_change > greatest_increase_profits:
            greatest_increase_profits = monthly_change
            greatest_increase_date = row[0]

        if monthly_change < greatest_decrease_profits:
            greatest_decrease_profits = monthly_change
            greatest_decrease_date = row[0]


        previous_rev = current_rev
        
print("total_net:" + str(total_net))
average_rev = (total_net/ total_months)
print(average_rev)
print("average_rev:" + str(average_rev))
average_change = total_monthly_change/ (total_months-1)
print("Greatest Increase:" + str(greatest_increase_profits))
print("Greatest Increase Date:" + str(greatest_increase_date))
print("Greatest Decrease:" + str(greatest_decrease_profits))
print("Greatest Decrease Date:" + str(greatest_decrease_date))



print("Complete")


output = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total Profit: ${total_net}\n"
   f"Average  Change: ${average_change:.2f}\n"
   f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_profits})\n"
   f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_profits})\n")


print(output)
with open(file_to_output, "w") as txt_file:
   txt_file.write(output)


print("Total Net: $" + str(total_net))
print("Average Revenue:"+ str(average_rev))


total_net = 0



#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.