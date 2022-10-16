class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s = Counter(nums)
        res = 0
        
        for x in s:
            if k == 0 and s[x] >= 2 or k != 0 and k + x in s:
                res += 1

        return res