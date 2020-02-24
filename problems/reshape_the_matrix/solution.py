class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        row = len(nums)
        column = len(nums[0])

        if row<=r and column<=c:
            return nums


        lst = [x for i in nums for x in i]
        count = 0
        ans = []

        for _ in range(r):
            temp = []

            for _ in range(c):
                temp.append(lst[count])
                count+=1
            ans.append(temp)

        
        return ans