class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        def compare(a,b):
            return a if a[0] < b[0] or (a[0] == b[0] and a[1] < b[1]) else b
        
        mp = collections.defaultdict(list)
        res = float('-inf')
        for i, t1 in enumerate(towers):
            s = 0
            for j, t2 in enumerate(towers):
                x1,y1 = t1[0], t1[1]
                x2,y2 = t2[0], t2[1]
                x = abs(x1-x2)
                y = abs(y1-y2)
                distance = x**2 + y**2
                
                quality = abs(t2[2] / (1 + math.sqrt(distance)))
                if math.sqrt(distance) <= radius:
                    s += int(quality)
                    
            res = max(res, s)

            if s in mp:
                mp[s] = compare(mp[s], [t1[0],t1[1]])
            else:
                mp[s] = [t1[0],t1[1]]

        return mp[res]