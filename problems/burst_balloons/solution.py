class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        n = len(nums) - 1
        mp = [[0 for i in range(n)] for j in range(n)]
        
        for p in range(1,n):
            for j in range(p, n):
                i = j - p
                mp[i][j] = max(
                    mp[i][k] + mp[k+1][j] + \
                      nums[i] * nums[k+1] * nums[j+1]
                    
                    for k in range(i,j)
                )
        
        return mp[0][n-1]