class DetectSquares:

    def __init__(self):
        self.xmap = collections.defaultdict(set)
        self.mp = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.mp[tuple(point)] += 1
        self.xmap[point[0]].add(point[1])

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        
        for y2 in self.xmap[x1]:
            d = abs(y2 - y1)
            if d == 0: continue
            for x3, y3 in [(x1 + d, y1), (x1 - d, y1)]:
                x4, y4 = x3, y2
                
                res += self.mp[(x1, y2)] * self.mp[(x3, y3)] * self.mp[(x4, y4)]
        
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)