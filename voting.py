"""
TASK: Create a VotingSystem class.

Requirements:
1. The class should allow registering candidates.
2. Each candidate should start with 0 votes.
3. The class should allow voters (using voter IDs) to cast votes.
   - Ensure one voter cannot vote more than once.
4. Provide a method to display election results.

Example Usage:
    election = VotingSystem()
    election.register_candidate("Alice")
    election.register_candidate("Bob")
    election.vote("Voter1", "Alice")
    election.vote("Voter2", "Bob")
    election.vote("Voter3", "Alice")
    print(election.results())  # {"Alice": 2, "Bob": 1}
    print(election.winner()) # Alice
"""
class VotingSystem:
    def __init__(self):
        self.candidates={}
        self.voters=()
    def register_candidate(self,candidate):
        self.candidates[candidate]=0
    def vote(self, voterID, candidate):
        if voterID in self.voters:
            return "You have already voted"
        elif candidate not in self.candidates:
            return "Candidate does not exist"
        else:
            self.candidates[candidate]+=1
            self.voters+=(voterID,)
    def results(self):
        return self.candidates
    def winner(self):
        max_votes=0
        for candidate in self.candidates:
            if self.candidates[candidate]>max_votes:
                max_votes= self.candidates[candidate]
                winner= candidate
            elif self.candidates[candidate]==max_votes:
                winner= winner+" "+candidate
            else:
                continue
        return winner




election = VotingSystem()
election.register_candidate("Alice")
election.register_candidate("Bob")
print(election.results())
election.vote("Voter1", "Alice")
election.vote("Voter2", "Bob")
election.vote("Voter3", "Alice")
print(election.results())
print(election.winner())