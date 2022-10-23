class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        A = sorted(nums, key = lambda x : (x & 1, x))
        B = sorted(target, key = lambda x : (x & 1, x))
        res = 0
        
        for a, b in zip(A, B):
            if a > b:
                res += a - b

        return res // 2