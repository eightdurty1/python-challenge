#Import CSV and OS Modules
import csv
import os


#Variables
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

#Sortes results by vote count in descending order
results.sort(key=lambda x:x[2], reverse=True)
#Determines the candidate with highest vote count
candidate_winner = results[0][0]

#Stores final analysis values as strings into a tuple
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

#Joins the final analysis strings into a single string with newline 
final_results_string = '\n'.join(final_analysis)
print(final_results_string)

#Prints each candidate's name, votes and vote count
for candidate_name, percentage_vote, vote_count in results:
    print(f"{candidate_name}: {percentage_vote:3f}% ({vote_count})")


# Export results to to .txt file
with open('final_election_results.txt', mode='w') as file:
    file.write(final_results_string)
    







