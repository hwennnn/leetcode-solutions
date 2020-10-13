class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        
        prefix, suffix = [0], [0]
        
        for v in arr:
            prefix.append(prefix[-1] + v)
        
        for v in arr[::-1]:
            suffix.append(suffix[-1] + v)
            
        res = float("-inf")
        
        for i in range(k+1):
            res = max(res, prefix[i] + suffix[k-i])
        
        return res