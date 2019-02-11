# Dependencies
import csv

# Load files
file_to_load = "Resources/budget_data.csv"
file_to_output = "Resources/budget_analysis.txt"

# declare Variables
total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999999]
revenue_changes = []

# Files reading
with open(file_to_load) as data_revenue:
    reader = csv.DictReader(data_revenue)

# Loop through rows of data and get the totals
    for row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        revenue_change = int(row["Profit/Losses"]) - prev_revenue

# Reset the value of prev_revenue to the row I completed my analysis
    prev_revenue = int(row["Profit/Losses"])

# Determine the greatest increase

    if (revenue_change > greatest_increase[1]):
        greatest_increase[1] = revenue_change
        greatest_increase[0] = row["Date"]

    if (revenue_change < greatest_decrease[1]):
        greatest_decrease[1] = revenue_change
        greatest_decrease[0] = row["Date"]

# Add to the revenue_changes list and set revenue average
    revenue_changes.append(int(row["Profit/Losses"]))
    revenue_avg = sum(revenue_changes) / len(revenue_changes)

# Print Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

