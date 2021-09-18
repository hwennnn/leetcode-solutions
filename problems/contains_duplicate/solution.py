class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sset = set()
        
        for x in nums:
            if x in sset: return True
            sset.add(x)
        
        return False