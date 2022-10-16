class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        available = list(range(n))
        mp = collections.defaultdict(int)
        seats = []
        
        for i, (t1,t2) in enumerate(times):
            seats.append((t1, 1, i))
            seats.append((t2, 0, i))
        
        seats.sort()
        
        for time, isArrival, friend in seats:
            if isArrival:
                seat = heapq.heappop(available)
                if friend == targetFriend: return seat
                mp[friend] = seat
            else:
                seat = mp[friend]
                heapq.heappush(available, seat)
        
        return mp[targetFriend]