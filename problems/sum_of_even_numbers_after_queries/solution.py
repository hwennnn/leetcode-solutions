class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        odd = even = 0
        res = []
        
        for x in nums:
            if x % 2 == 0:
                even += x
            else:
                odd += x
        
        for val, index in queries:
            updated = nums[index] + val
            if nums[index] % 2 == 0:
                if updated % 2 == 0:
                    even += val
                else:
                    even -= nums[index]
                    odd += updated
            else:
                if updated % 2 == 0:
                    odd -= nums[index]
                    even += updated
                else:
                    odd += val
            
            res.append(even)
            nums[index] = updated
        
        return res