class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        good = 0
        
        mp = defaultdict(int)
        # j - i != nums[j] - nums[i]
        # Bad = j - nums[j] != i - nums[i]
        
        for i, x in enumerate(nums):
            good += mp[x - i]
            mp[x - i] += 1
        
        return total - good