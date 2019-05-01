import csv
import os

budget_path = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("election_results.txt")


Votes_path = “”
Total = 0
Candidates = []
Can_wins = {}
Can_tot = {}
Winner = “”


with open(election_data) as election_data:
    reader = csv.reader(election_data)

    # Read the header row
    header = next(reader)s
    print(header)

    first_row = next(reader)
    print(first_row)
    
    print(first_row[0])
    print(first_row[1])
    rev = int(first_row[1])
    candidate_total = Candidate + rev
    previous_candidate = rev
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
        
        if monthly_change > Can_wins:
            greatest_increase_profits = monthly_change
            greatest_increase_date = row[0]

        if monthly_change < Can_tot:
            greatest_decrease_profits = monthly_change
            greatest_decrease_date = row[0]


        previous_rev = current_rev
        
print("Total Votes:" + str(Total))
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
   f"\nVote-Counting\n"
   f"----------------------------\n"
   f"Total: {total_months}\n"
   f"Candidates: ${total_net}\n"
   f"Can_wins: ${average_change:.2f}\n"
   f"Can_tot: {greatest_increase_date} (${greatest_increase_profits})\n"
   f"Winner: {greatest_decrease_date} (${greatest_decrease_profits})\n")


Votes_path = “”
Total = 0
Candidates = []
Can_wins = {}
Can_tot = {}
Winner = “”

print(output)
with open(file_to_output, "w") as txt_file:
   txt_file.write(output)



#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.