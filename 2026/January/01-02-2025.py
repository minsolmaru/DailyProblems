"""
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. 
Write a program that reads this file as a stream and returns the top 3 candidates at any given time. If you find a voter voting more than once, report this as fraud.
"""

import heapq
from collections import defaultdict

class VotingStream:
    def __init__(self):
        self.seen_voters = set()
        self.vote_count = defaultdict(int)
        self.top3 = [] 

    def process_vote(self, voter_id, candidate_id):
        # Fraud detection
        if voter_id in self.seen_voters:
            print(f"FRAUD DETECTED: voter {voter_id}")
            return

        self.seen_voters.add(voter_id)

        # Update vote count
        self.vote_count[candidate_id] += 1
        count = self.vote_count[candidate_id]

        # Remove outdated entry if present
        self.top3 = [(c, cid) for c, cid in self.top3 if cid != candidate_id]
        heapq.heapify(self.top3)

        # Push updated candidate
        heapq.heappush(self.top3, (count, candidate_id))

        # Keep only top 3
        if len(self.top3) > 3:
            heapq.heappop(self.top3)

    def get_top3(self):
        return sorted(self.top3, reverse=True)
    

stream = VotingStream()

votes = [
    (1, "A"),
    (2, "B"),
    (3, "A"),
    (4, "C"),
    (5, "A"),
    (1, "B")  # fraud
]

for v in votes:
    stream.process_vote(*v)
    print(stream.get_top3())

