class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        once = defaultdict(int)
        twice = defaultdict(int)
        complete = defaultdict(int)
        
        for num in nums:
            if once[num - 1]:
                once[num - 1] -= 1
                twice[num] += 1
            elif twice[num - 1]:
                twice[num - 1] -= 1
                complete[num] += 1
            elif complete[num - 1]:
                complete[num - 1] -= 1
                complete[num] += 1
            else:
                once[num] += 1
        
        return sum(once.values()) + sum(twice.values()) == 0
