class Solution:
    def busyStudent(self, start: List[int], end: List[int], k: int) -> int:
        
        res = 0
        for i,j in zip(start, end):
            if k >= i and k <= j:
                res += 1
        
        return res