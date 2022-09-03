class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        
        def go(index, curr):
            if index == n:
                res.append(curr)
                return
            
            last = curr % 10
            
            for nxt in {last + k, last - k}:
                if 0 <= nxt < 10:
                    go(index + 1, curr * 10 + nxt)
        
        for x in range(1, 10):
            go(1, x)
        
        return res