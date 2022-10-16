class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, end: int) -> int:
        a = min(start, end)
        b = max(start, end)
        
        return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))