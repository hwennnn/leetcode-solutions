class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        
        sort = sorted(nums)[::-1]
        
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4,len(nums)+1)]
        
        temp = dict(zip(sort,rank))
        
        return list(map(temp.get,nums))