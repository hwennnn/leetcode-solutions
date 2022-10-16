class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        bits = [0] * 32
        res = [0] * N
        j = N - 1
        curr = target = 0
        
        for i in range(N - 1, -1, -1):
            target |= nums[i]
            curr |= nums[i]
            
            for k in range(31, -1, -1):
                if (nums[i] & (1 << k)) > 0:
                    bits[k] += 1
            
            while curr == target and i <= j:
                for k in range(31, -1, -1):
                    if (nums[j] & (1 << k)) > 0:
                        bits[k] -= 1
                        if bits[k] == 0:
                            curr ^= (1 << k)
                
                j -= 1
            
            res[i] = j - i + 2
            
        return res