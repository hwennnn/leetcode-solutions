class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        kIndex = nums.index(k)
        t = nums[kIndex]
        res = 0
        
        ld = rd = 0
        left, right = defaultdict(int), defaultdict(int)
        left[0] = right[0] = 1
        
        for index in range(kIndex + 1, N):
            if nums[index] > t:
                rd += 1
            else:
                rd -= 1
            
            right[rd] += 1
        
        for index in range(kIndex - 1, -1, -1):
            if nums[index] > t:
                ld += 1
            else:
                ld -= 1
            
            left[ld] += 1
        
        for x in left.keys():
            res += left[x] * right[-x]
            res += left[x] * right[-x + 1]

        return res
                
            