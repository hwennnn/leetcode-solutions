class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, reverse=True)
        print(points)
        ret, shoot = 0, float('inf')
        for s, e in points:
            if shoot > e:
                shoot = s
                ret += 1
        return ret