class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        available = [-startFuel]
        res, curr = -1, 0
        i = 0
        
        while available and curr < target:
            fuel = -(heapq.heappop(available))
            res += 1
            curr += fuel
            
            while i < len(stations) and curr >= stations[i][0]:
                heapq.heappush(available, -stations[i][1])
                i += 1
            
        return res if curr >= target else -1