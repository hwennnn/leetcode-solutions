class Solution:
    def minOperationsMaxProfit(self, customers: List[int], bc: int, rc: int) -> int:
        
        peak = res = idx = cust = i = 0
        
        while cust > 0 or i < len(customers):
            if i < len(customers):
                cust += customers[i]
            
            c = min(cust, 4)
            res += c * bc - rc
            
            if res > peak:
                peak = res
                idx = i + 1
            
            cust -= c
            i += 1
        
        return idx if idx > 0 else -1