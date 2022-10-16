class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        usedCount = [0] * n
        
        availableRooms = list(range(n))
        usedRooms = []
        
        for start, end in meetings:
            while usedRooms and usedRooms[0][0] <= start:
                t, roomId = heappop(usedRooms)
                heappush(availableRooms, roomId)
            
            if availableRooms:
                r = heappop(availableRooms)
                heappush(usedRooms, (end, r))
            else:
                endTime, r = heappop(usedRooms)
                heappush(usedRooms, (endTime + end - start, r))
                
            usedCount[r] += 1
            
        return usedCount.index(max(usedCount))