class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        
        while target > 1:
            if target % 2 == 0:
                if maxDoubles > 0:
                    target //= 2
                    maxDoubles -= 1
                    res += 1
                else:
                    return res + target - 1
            else:
                target -= 1
                res += 1
        
        return res