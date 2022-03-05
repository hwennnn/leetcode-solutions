class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        
        for i, x in enumerate(arr):
            res += x * math.ceil(((i + 1) * (n - i)) / 2)
        
        return res