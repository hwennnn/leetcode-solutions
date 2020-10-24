class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        mp = collections.defaultdict(int)
        
        for i,v in enumerate(nums):
            if t - v not in mp:
                mp[v] = i
            else:
                return [mp[t-v], i]