class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        res = 0
        
        for num in cnt:
            if num + 1 in cnt:
                res = max(res, cnt[num] + cnt[num + 1])
        
        return res