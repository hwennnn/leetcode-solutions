class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        total = sum(x for x in nums if x % 2 == 0)
        res = []
        
        for val, index in queries:
            x = nums[index]
            newNum = x + val
            nums[index] = newNum
            
            if x % 2 == 0:
                if newNum % 2 == 0:
                    total += newNum - x
                else:
                    total -= x
            else:
                if newNum % 2 == 0:
                    total += newNum
            
            res.append(total)
        
        return res