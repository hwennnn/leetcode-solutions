class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        def good(x):
            t = 0
            
            for i, d in enumerate(dist):
                if i != n - 1:
                    h = math.ceil(d / x)
                else:
                    h = d / x

                t += h

            return t <= hour
            

        left, right = 1, 10 ** 7 + 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if left <= 10 ** 7 else -1
            
        