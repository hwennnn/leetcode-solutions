class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mp = collections.defaultdict(int)
        mmax = 0
        
        for x in nums: mmax |= x
        
        for mask in range(1, 1 << n):
            s = 0
            for j in range(n):
                if (mask >> j) & 1:
                    s |= nums[j]

            mp[s] += 1

        return mp[mmax]