class Solution:
    def maximumNumber(self, nums: str, change: List[int]) -> str:
        nums = list(nums)
        done = False
        
        for i, num in enumerate(nums):
            pos = int(num)
            if change[pos] >= pos:
                nums[i] = str(change[pos])
                if change[pos] > pos:
                    done = True
            else:
                if done:
                    break
        
        return "".join(nums)