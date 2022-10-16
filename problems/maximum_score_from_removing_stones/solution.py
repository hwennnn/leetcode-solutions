from heapq import heappush, heappop, heapify

class Solution:
    # heap
    def maximumScore(self, a: int, b: int, c: int) -> int:
        return min((a+b+c)//2 , a+b+c - max(a,b,c))
        res = 0
        stones = [-a,-b,-c]
        heapify(stones)
        
        while abs(stones[0]) > 0 and abs(stones[1]) > 0:
            first = heappop(stones) + 1
            second = heappop(stones) + 1
            
            heappush(stones, first)
            heappush(stones, second)
            
            res += 1
            
        return res
            
            