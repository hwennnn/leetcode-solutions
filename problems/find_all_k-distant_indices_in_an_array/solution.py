class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = [i for i, x in enumerate(nums) if x == key]
        res = []
        
        for i in range(n):
            for j in indices:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        
        return res