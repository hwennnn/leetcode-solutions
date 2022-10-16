class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        pq = deque(passengers)
        
        P = set(passengers)
        res = -inf
        
        if pq[0] - 1 <= buses[0]:
            res = pq[0] - 1
        
        for time in buses:
            cap = 0
            
            while pq and pq[0] <= time and cap < capacity:
                t = pq.popleft()
                
                if t - 1 not in P and t - 1 <= time:
                    res = max(res, t - 1)
                
                if cap + 1 != capacity and t + 1 not in P and t + 1 <= time:
                    res = max(res, t + 1)
                
                cap += 1
            
            if cap < capacity and time not in P:
                res = max(res, time)
                
        return res