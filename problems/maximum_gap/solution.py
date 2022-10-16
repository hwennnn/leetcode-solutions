class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        
        mmax, mmin = float('-inf'), float('inf')
        
        for num in nums:
            mmax = max(mmax, num)
            mmin = min(mmin, num)
        
        gap = math.ceil((mmax - mmin) / (n - 1)) or 1
        bucket_max = [float('-inf') for _ in range(n)]
        bucket_min = [float('inf') for _ in range(n)]
        
        for num in nums:
            index = (num - mmin) // gap
            bucket_max[index] = max(bucket_max[index], num)
            bucket_min[index] = min(bucket_min[index], num)

        maxGap = float('-inf')
        prevMax = mmin
        
        for i in range(n):
            if bucket_max[i] == float('-inf') and bucket_min[i] == float('inf'): continue
            
            maxGap = max(maxGap, bucket_min[i] - prevMax)
            prevMax = bucket_max[i]
        
        return maxGap