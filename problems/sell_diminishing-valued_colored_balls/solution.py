from heapq import heappop, heappush

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        M = 10 ** 9 + 7
        
        pq = []
        for v in inventory:
            heappush(pq, (-v, 1))

        res = 0
        
        while pq and orders > 0:
            top, count = pq[0]
            top = -top
            heappop(pq)
            
            while pq and top == -pq[0][0]:
                count += pq[0][1]
                heappop(pq)
            
            nextTop = 0
            if pq:
                nextTop = -pq[0][0]
                
            delta = top - nextTop
            
            if delta * count <= orders:
                d = (top*(top+1)) // 2
                d -= (nextTop*(nextTop+1)) // 2
                d *= count
                
                res += d
                res %= M
                orders -= (delta*count)
            
            else:
                cnt = orders // count
                d = (top*(top+1)) // 2
                nextTop = top - cnt
                d -= (nextTop*(nextTop+1)) // 2
                d *= count
                
                res += d
                res %= M
                orders -= (count * cnt)
                
                leftover = orders % count
                res += nextTop * leftover
                res %= M
                
                orders -= leftover
                
            if nextTop:
                heappush(pq, (-nextTop, count))
            
                        
        return res % M