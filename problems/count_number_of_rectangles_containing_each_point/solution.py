class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(rectangles)
        res = []
        mp = defaultdict(list)

        for x, y in rectangles:
            mp[y].append(x)
        
        for k, v in mp.items():
            v.sort()
        
        for x, y in points:
            count = 0
            
            for z in range(y, 101):
                l = mp[z]
                
                xIndex = bisect.bisect_left(l, x)

                count += len(l) - xIndex
                    
            res.append(count)
        
        return res