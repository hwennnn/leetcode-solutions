from heapq import heappop,heappush

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        
        buy, sell = [], []
        
        for price,amt,ot in orders:
            if ot == 0:
                heappush(buy, [-price, amt])
            else:
                heappush(sell, [price, amt])
            
            while sell and buy and -buy[0][0] >= sell[0][0]:
                to_deduct = min(buy[0][1], sell[0][1])
                buy[0][1] -= to_deduct
                sell[0][1] -= to_deduct
                
                if buy[0][1] == 0: heappop(buy)
                if sell[0][1] == 0: heappop(sell)
        
        return sum(amt for price,amt in buy+sell) % M