class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 2
        
        count = Counter(nums)
        
        for k, v in count.items():
            if v == n:
                return k