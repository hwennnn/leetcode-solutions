class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        visited = [0] * n
        
        for i in range(n):
            count = 0
            
            while not visited[i]:
                visited[i], count, i = 1, count + 1, nums[i]
            
            res = max(res, count)
        
        return res