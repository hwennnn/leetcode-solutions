class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        divider = n*2//2
        first_half = nums[:divider]
        second_half = nums[divider:]
        ans = []
        
        for i in range(divider):
            ans.append(first_half[i])
            ans.append(second_half[i])

        return ans