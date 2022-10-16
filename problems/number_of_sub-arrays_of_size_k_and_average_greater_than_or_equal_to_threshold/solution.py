class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        prefix = [0] * (n+1)
        res = 0
        
        for i,num in enumerate(arr):
            prefix[i+1] += prefix[i] + num
        
        for i in range(n-k+1):
            if (prefix[i+k] - prefix[i]) >= threshold * k:
                res += 1
        
        return res