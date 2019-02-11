# Dependencies
import csv
from collections import OrderedDict
from operator import itemgetter

# Load files
file_to_load = "Resources/election_data.csv"
file_to_output = "Resources/election_analysis.txt"

# declare Variables
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

# Files reading
with open(file_to_load) as data_election:
    reader = csv.DictReader(data_election)
    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

    if row["Candidate"] not in candidate_options:
        candidate_options.append(row["Candidate"])
        candidate_votes[row["Candidate"]] = 1

    else:
        candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1


# find the Winner:
if (votes > winner_votes[2]):
greatest_increase[1] = revenue_change
greatest_increase[0] = row["Candidate"]
#print()
#print()
#print()
print("Election Results")
print("-------------------------")
print("Total Votes " + str(votes))
print("-------------------------")
#results
for candidate in candidate_votes:
    print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    candidate_votes  
    winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")

#File Output
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))