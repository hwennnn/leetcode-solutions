class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        arr = [0] * 60
        
        for t in time:
            t %= 60
            res += arr[(60-t)%60]
            arr[t] += 1
            
        return res