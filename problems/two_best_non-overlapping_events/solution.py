class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        A = []
        
        for start, end, value in events:
            A.append((start, 1, value))
            A.append((end + 1, -1, value))
        
        A.sort()
        currMax = res = 0
        
        for curr, t, x in A:
            if t == 1:
                res = max(res, currMax + x)
            else:
                currMax = max(currMax, x)
        
        return res