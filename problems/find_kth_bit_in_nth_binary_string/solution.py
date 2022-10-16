class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        @cache
        def go(x):
            if x <= 1: return "0"
            
            last = go(x - 1)
            
            r = "".join(["1" if c == "0" else "0" for c in last])
            
            return go(x - 1) + "1" + r[::-1]
        
        return go(n)[k - 1]