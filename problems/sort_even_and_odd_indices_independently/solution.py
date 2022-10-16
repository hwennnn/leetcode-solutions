class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd, even = [], []
        
        for i, x in enumerate(nums):
            if i & 1:
                odd.append(x)
            else:
                even.append(x)
        
        odd.sort(key = lambda x: -x)
        even.sort()
        
        res = [-1] * n
        index = 0
        
        for i in range(0, n, 2):
            res[i] = even[index]
            index += 1
        
        index = 0
        
        for i in range(1, n, 2):
            res[i] = odd[index]
            index += 1
        
        return res