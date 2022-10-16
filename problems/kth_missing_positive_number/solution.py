class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 1
        
        s = set(arr)
        
        while k > 0 and start <= 1000:
            if start not in s: k -= 1
                
            start += 1
        
        if k > 0: start += k
        
        return start - 1
        