class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mp = collections.defaultdict(int)
        res = 0

        for x in time:
            x %= 60
            res += mp[(60 - x) % 60]
            mp[x] += 1
        
        return res
        
        
        