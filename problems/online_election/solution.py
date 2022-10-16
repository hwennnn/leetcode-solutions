class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        mp = defaultdict(int)
        self.times = times
        self.leads = []
        lead = -1
        
        for p, t in zip(persons, times):
            mp[p] += 1
            if mp[p] >= mp[lead]:
                lead = p
            self.leads.append(lead)
            
    def q(self, t: int) -> int:
        index = bisect.bisect_right(self.times, t) - 1
        
        return self.leads[index]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)