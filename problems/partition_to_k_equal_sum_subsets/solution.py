class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0: return False
        
        target = total // k
        nums.sort(reverse = 1)
        
        @cache
        def go(mask):
            curr = 0
            
            for i in range(n):
                if (mask >> i) & 1 > 0:
                    curr += nums[i]
            
            done, side = divmod(curr, target)
            
            if done == k - 1: return True
            
            for i in range(n):
                if (mask & (1 << i)) == 0:
                    if side + nums[i] <= target and go(mask | (1 << i)):
                        return True
            
            return False
        
        return go(0)