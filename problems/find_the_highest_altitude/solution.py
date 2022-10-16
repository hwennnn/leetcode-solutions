class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for g in gain:
            res.append(res[-1]+g)
        
        return max(res)
        