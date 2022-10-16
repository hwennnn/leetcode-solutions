from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.nums[:]
        
        for i in range(self.n):
            index = randint(i, self.n - 1)
            res[i], res[index] = res[index], res[i]
        
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()