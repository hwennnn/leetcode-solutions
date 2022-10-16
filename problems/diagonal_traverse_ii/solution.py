class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        mp = collections.defaultdict(list)
        
        for i, r in enumerate(nums):
            for j,v in enumerate(r):
                mp[i+j].append(v)
                
        return [v for key in mp for v in mp[key][::-1] ]
        