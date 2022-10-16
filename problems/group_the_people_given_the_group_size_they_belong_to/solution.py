class Solution:
    def groupThePeople(self, arr: List[int]) -> List[List[int]]:
        mp = collections.defaultdict(list)
        
        for i,x in enumerate(arr):
            mp[x].append(i)
        
        res = []
        
        for key in mp:
            groups = mp[key]
            n = len(groups)
            
            if n == key:
                res.append(groups)
            else:
                for i in range(0, n, key):
                    res.append(groups[i:i+key])
        
        return res