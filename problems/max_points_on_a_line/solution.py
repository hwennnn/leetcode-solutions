class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        INT_MAX = 10 ** 5
        
        for i in range(n):
            x1, y1 = points[i]
            mp = collections.defaultdict(int)
            samePoints = 1
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    samePoints += 1
                elif x1 == x2:
                    mp[INT_MAX] += 1
                else:
                    x, y = x2 - x1, y2 - y1
                    divisor = gcd(x, y)
                    x, y = x // divisor, y // divisor
                    mp[y / x] += 1

            mmax = max(mp.values() or [0])
            mmax += samePoints
            res = max(res, mmax)
                    
        return res