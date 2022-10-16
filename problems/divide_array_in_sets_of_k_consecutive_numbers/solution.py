class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0: return False
        
        count = collections.Counter(nums)
        keys = sorted(count)
        
        for key in keys:
            if count[key] > 0:
                c = count[key]
                for i in range(key, key+k):
                    if count[i] < c: return False
                    
                    count[i] -= c
            
        return True