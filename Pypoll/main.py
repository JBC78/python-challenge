# Voter ID,County,Candidate
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

import os
import csv

#Set lists
voter = []
get_votes = []

# directory path
dirname = os.path.dirname(__file__)
election_data = os.path.join(dirname,'Resources', 'election_data.csv')

# open election_data.csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header row and skip
    csv_header = next(csvreader)
    
    #creates dictionary using canditate column in file, count votes for each candidate and tracks total
    for row in csvreader:
        voter.append(row[0])
        get_votes.append(row[2])

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(voter)}")
print("-------------------------")

# sort candidates votes by candidate A to Z
candidates = list(set(get_votes))
candidates.sort()
# get a vote count for each candidate
candVotes = []
for cand in candidates:
    candVotes.append(get_votes.count(cand))

for i in range(len(candidates)):
    print(f"{candidates[i]}: {'{:.2%}'.format(candVotes[i]/len(get_votes))} ({candVotes[i]})")
print("-------------------------")
print(f"Winner: {candidates[candVotes.index(max(candVotes))]}")
print("-------------------------\n")

# print to Analysis folder
election_results = os.path.join(dirname, 'Analysis', 'election_results.txt')
with open(election_results, 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {len(voter)}\n")
    text.write("-------------------------\n")
    text.write(f"Total: ${candidates[i]}: {'{:.2%}'.format(candVotes[i]/len(get_votes))} ({candVotes[i]}\n")
    text.write("-------------------------\n")
    text.write(f"Winner: {candidates[candVotes.index(max(candVotes))]})\n")