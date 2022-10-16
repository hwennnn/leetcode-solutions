class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = list(accumulate(months, initial = 0))
        
        def f(x):
            month, day = map(int, x.split("-"))
            
            return prefix[month - 1] + day
        
        a, b, c, d = map(f, (arriveAlice, leaveAlice, arriveBob, leaveBob))
        
        return max(0, min(b, d) - max(a, c) + 1)