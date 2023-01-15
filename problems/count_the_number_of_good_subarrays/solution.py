class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cnt = defaultdict(int)
        pairs = 0
        res = 0
        i = 0
        
        for j, x in enumerate(nums):
            pairs += cnt[x]
            cnt[x] += 1
            
            while pairs >= k:
                res += (N - j)
                pairs -= cnt[nums[i]] - 1
                cnt[nums[i]] -= 1
                i += 1
        
        return res