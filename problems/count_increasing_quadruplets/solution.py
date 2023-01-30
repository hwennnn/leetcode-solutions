class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        N = len(nums)
        left = [[0] * (N + 1)] # 0...i, < j
        right = [[0] * (N + 1)] # i+1...N, > j
        
        for i in range(1, N):
            curr = left[-1][:]
            
            for j in range(nums[i - 1] + 1, N + 1):
                curr[j] += 1
            
            left.append(curr)
        
        for i in range(N - 2, -1, -1):
            curr = right[-1][:]
            
            for j in range(nums[i + 1]):
                curr[j] += 1
            
            right.append(curr)
            
        right.reverse()
        
        res = 0
        
        for j in range(N):
            for k in range(j + 1, N):
                if nums[k] < nums[j]:
                    res += left[j][nums[k]] * right[k][nums[j]]
        
        return res