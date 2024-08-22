# Import CSV and OS modules
import csv
import os
#print(os.getcwd())

# Stores total number of months
total_months = 0

# Stores net total amount of P&L
net_total = 0

# Stores changes in P&L
changes_profit_loss = []

#Stores P&L from pervious months
previous_profit_loss = None

#Stores greatest increase in profits date and amount
greatest_profit_increase = {
    "date": "", 
    "amount": float('-inf')
}
#stores greatest decrease in profits data and amount
greatest_profit_decrease = {
    "date": "",
    "amount": float('inf')
}


#File Path
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#print(budget_data_csv)

# Opens the CSV file. Calculates total months nad the net total amount of P&L over a taime period.
with open(budget_data_csv, mode="r") as file:
    csv_reader = csv.DictReader(file)
    # Loop through every row in the CSV
    for row in csv_reader:
        #Count total of months
        total_months = total_months + 1
        #Add the current months profit/loss to net total
        net_total = net_total + int(row["Profit/Losses"])
        #print(f"Net Total: {net_total}")
        #print(row["Date"])
       #print(total_months)


        #Calulcates the changes from the previous month
        if previous_profit_loss is not None:
            change = int(row["Profit/Losses"]) - previous_profit_loss
            changes_profit_loss.append(change)
            #print("Currently running this line")

            #Checks for the greatest increse / decrease
            if change > greatest_profit_increase["amount"]:
                greatest_profit_increase = {
                    "date": row["Date"],
                    "amount": change
                }
            if change < greatest_profit_decrease ["amount"]:
                greatest_profit_decrease = {
                    "date": row["Date"],
                    "amount": change
                }



        previous_profit_loss = int(row["Profit/Losses"])
#Calculatte average change
#average_change = sum(changes_profit_loss) / sum(changes_profit_loss) #if changes_profit_loss else 0
if changes_profit_loss:
    average_change = sum(changes_profit_loss) / len(changes_profit_loss)
else:
    average_change = 0


final_analysis = (
    f"Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change}",
    f"Greatest Increase in Profits: {greatest_profit_increase['date']} ({greatest_profit_increase['amount']})",
    f"Greatest Decrease in Profits: {greatest_profit_decrease['date']} ({greatest_profit_decrease['amount']})",

)

#Converts tuple into string and formats the line break
final_analysis_string = '\n'.join(final_analysis)

#Print analysis to the terminal
print(final_analysis_string)

#Exports the results to a TXT file
with open('financial_analysis.txt', mode='w') as file:
    file.write(final_analysis_string)






















