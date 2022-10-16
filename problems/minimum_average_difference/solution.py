class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        mmin = float('inf')
        res = -1
        n = len(nums)
        curr = 0
        s = sum(nums)
        

        for i, x in enumerate(nums):
            left = i + 1
            right = n - i - 1
            
            curr += x
            s -= x

            if i == n - 1:
                ans = abs(floor(curr / left))
            else:
                ans = abs(floor(curr / left) - floor(s / right))
            # print(i, ans)
            if ans < mmin:
                mmin = ans
                res = i
        
        return res