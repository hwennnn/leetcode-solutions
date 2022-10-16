class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        res = 0
        last7 = deque()
        last30 = deque()
        
        for day in days:
            while last7 and day >= last7[0][0]:
                last7.popleft()
            
            while last30 and day >= last30[0][0]:
                last30.popleft()
            
            last7.append((day + 7, res + costs[1]))
            last30.append((day + 30, res + costs[2]))
            
            res = min(res + costs[0], last7[0][1], last30[0][1])
        
        return res