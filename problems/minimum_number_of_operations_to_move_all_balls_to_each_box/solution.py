class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = []
        
        for i in range(n):
            moves = 0
            for k in range(i):
                if boxes[k] == "1":
                    moves += i - k
            
            for k in range(i+1, n):
                if boxes[k] == "1":
                    moves += k - i
            
            res.append(moves)
        
        return res
            