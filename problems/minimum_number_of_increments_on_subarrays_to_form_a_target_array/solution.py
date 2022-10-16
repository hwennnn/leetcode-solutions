class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = x = target[0]
        
        for num in target:
            if num <= x:
                x = num
            else:
                res += num - x
                x = num
        
        return res