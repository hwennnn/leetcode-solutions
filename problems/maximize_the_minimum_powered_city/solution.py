class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)
        prefix = [0] * (N + 1)

        for i in range(N):
            left = max(0, i - r)
            right = min(N - 1, i + r)

            prefix[left] += stations[i]
            prefix[right + 1] -= stations[i]
        
        for i in range(1, N):
            prefix[i] += prefix[i - 1]

        def good(mid):
            stations = k
            build = [0] * (N + 1)

            for i in range(N):
                if i > 0:
                    build[i] += build[i - 1]
                
                curr = prefix[i] + build[i]

                if curr < mid:
                    need = mid - curr
                    stations -= need
                    if stations < 0:
                        return False
                    
                    j = min(i + r + r, N - 1)
                    build[i] += need
                    build[j + 1] -= need
            
            return stations >= 0

        left, right = 0, 10 ** 18
        res = 0

        while left <= right:
            mid = left + (right - left) // 2

            if good(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res