class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        
        prefix = [0] * (max(nums) + 1)
        counter = collections.Counter(nums)
        
        for num, count in counter.items():
            for j in range(num, len(prefix), num):
                prefix[j] += count
        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        return sum(prefix[num] for num in nums) % M