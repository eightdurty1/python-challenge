#Import CSV and OS Modules
import csv
import os

# Variables

#Total Votes
total_votes = 0
#List of cadidates
candidates_list = {}
#Stores the results
results = []

#File Path
election_data_csv = os.path.join("Resources", "election_data.csv")

#Opens CSV file
with open(election_data_csv, mode='r') as file:
    csv_reader = csv.DictReader(file)

    #Loop through ever row in the CSV file / increment total vote count
    for row in csv_reader:
        total_votes = total_votes + 1
        #print(total_votes)

        #Stores candidate name into a variable
        candidate_name = row['Candidate']

        #If condidional that increments candidate vote count
        if candidate_name in candidates_list:
            candidates_list[candidate_name] = candidates_list[candidate_name] + 1
        else: 
            candidates_list[candidate_name] = 1


#Loop all candidates for their vote count
for candidate_name in candidates_list:
    vote_count = candidates_list[candidate_name]

    #Percentage votes for each candidates
    percentage_vote = (vote_count/total_votes) * 100

    results.append((candidate_name, percentage_vote, vote_count ))

results.sort(key=lambda x:x[2], reverse=True)

candidate_winner = results[0][0]


final_analysis = (
    f"Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------",
    f"PLEASE SEE RESULTS BELOW",
    "-------------------------",
    f"Winner: {candidate_winner}",
    "-------------------------",
)

final_results_string = '\n'.join(final_analysis)

print(final_results_string)

for candidate_name, percentage_vote, vote_count in results:
    print(f"{candidate_name}: {percentage_vote:3f}% ({vote_count})")


# Export results to to .txt file
with open('final_election_results.txt', mode='w') as file:
    file.write(final_results_string)
    







