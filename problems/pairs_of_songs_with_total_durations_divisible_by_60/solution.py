class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        s = res = 0
        mp = Counter()
        
        for x in time:
            target = (60 - x) % 60
            
            res += mp[target]
            
            mp[x % 60] += 1
        
        return res