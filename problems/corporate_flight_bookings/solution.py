class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        
        for start,end,seats in bookings:
            res[start - 1] += seats
            res[end] -= seats
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        return res[:-1]