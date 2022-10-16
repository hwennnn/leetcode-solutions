class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], left: List[int], right: List[int]) -> List[bool]:
        res = []
        for l,r in zip(left,right):
            arr = sorted(nums[l:r+1])
            cd = abs(arr[1] - arr[0])
            check = True
            for i in range(2, len(arr)):
                if abs(arr[i] - arr[i-1]) != cd:
                    check = False
                    break
            
            res.append(check)
        
        return res