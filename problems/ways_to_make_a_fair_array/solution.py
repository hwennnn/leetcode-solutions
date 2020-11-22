class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd = even = 0
        res = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even += num
            else:
                odd += num
        
        co = ce = 0
        for i, num in enumerate(nums):
            e,o = even, odd
            if i % 2 == 0:
                ce += num
                e -= num
            else:
                co += num
                o -= num
                
            e -= (even - ce)
            e += (odd - co)
            o -= (odd - co)
            o += (even - ce)
                
            if (o == e):
                res += 1
        
        return res