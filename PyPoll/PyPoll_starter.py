import pandas as pd


file_path = '/System/Volumes/Data/Users/christinaland/Library/Mobile Documents/com~apple~CloudDocs/PyPoll/Resources/election_data.csv'


data = pd.read_csv(file_path)

# total number of votes cast
total_votes = data['Ballot ID'].count()

# list of candidates who received votes
candidates = data['Candidate'].unique()

# total votes for each candidate
votes_per_candidate = data['Candidate'].value_counts()

# percentage of votes each candidate won
vote_percentage = (votes_per_candidate / total_votes) * 100

# winner of the election
winner = votes_per_candidate.idxmax()
winner_votes = votes_per_candidate.max()

# Printresults
print(f"Total votes cast: {total_votes}\n")
print("Candidates and their results:")
for candidate in candidates:
print(f"{candidate}: {votes_per_candidate[candidate]} votes ({vote_percentage[candidate]:.2f}%)")
print(f"\nWinner: {winner} with {winner_votes} votes")
