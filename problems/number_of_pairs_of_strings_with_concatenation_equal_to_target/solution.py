class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        t = len(target)
        prefix = set()
        res = 0
        
        for i in range(1, t):
            prefix.add(target[:i])
        
        for i, word1 in enumerate(nums):
            if word1 in prefix:
                for j, word2 in enumerate(nums):
                    if i != j and word1 + word2 == target:
                        res += 1
        
        return res
                