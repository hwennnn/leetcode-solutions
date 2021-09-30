class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        
        @cache
        def dfs(mask, curr, done):
            if done == k - 1: return True
            if mask == 0: return False
        
            for j in range(n):
                if mask >> j & 1:
                    if nums[j] + curr == target:
                        if dfs(mask ^ (1 << j), 0, done + 1):
                            return True
                    elif nums[j] + curr < target:
                        if dfs(mask ^ (1 << j), curr + nums[j], done):
                            return True
            
            return False
        
        return dfs((1 << n) - 1, 0, 0)