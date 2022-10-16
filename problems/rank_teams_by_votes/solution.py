class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        mp = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        
        for v in votes:
            for i,t in enumerate(v):
                mp[t][i] -= 1
        
        return "".join(sorted(votes[0], key = mp.get))