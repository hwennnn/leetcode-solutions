class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        count = Counter()
        
        for i, x in enumerate(nums):
            if x == key:
                if i + 1 < n:
                    count[nums[i + 1]] += 1
        
        return count.most_common()[0][0]