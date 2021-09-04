class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        def backtrack(visited = set(), path = []):
            if len(path) == n:
                res.append(path)
                return
            
            for i in range(n):
                if i in visited: continue
                
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited: continue
                
                visited.add(i)
                backtrack(visited, path + [nums[i]])
                visited.remove(i)
        
        backtrack()
        return res