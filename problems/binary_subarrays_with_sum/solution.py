class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = Counter()
        count[0] = 1
        res = s = 0
        
        for x in nums:
            s += x
            
            res += count[s - goal]
            
            count[s] += 1
    
        return res