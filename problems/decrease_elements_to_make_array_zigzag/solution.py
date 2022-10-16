class Solution:
    def movesToMakeZigzag(self, A: List[int]) -> int:
        n = len(A)
        
        def helper(start):
            nums = A[:]
            count = 0
            
            for i in range(start, n, 2):
                if i - 1 >= 0 and nums[i] <= nums[i - 1]:
                    move = max(0, nums[i] - 1)
                    
                    if nums[i] > move:
                        count += abs(move - nums[i - 1])
                        nums[i - 1] = move
                    else:
                        return float('inf')
                
                if i + 1 < n and nums[i] <= nums[i + 1]:
                    move = max(0, nums[i] - 1)
                        
                    if nums[i] > move:
                        count += abs(move - nums[i + 1])
                        nums[i + 1] = move
                    else:
                        return float('inf')

            
            return count
        
        return min(helper(0), helper(1))
                