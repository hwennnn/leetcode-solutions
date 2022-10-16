class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
    
        for i,price in enumerate(prices):
            
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
                
            stack.append(i)
            
        return prices