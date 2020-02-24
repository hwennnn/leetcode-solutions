class Solution:
    def tribonacci(self, n: int) -> int:
        
        temp = {0:0, 1:1, 2:1}
        
        def tri(n):
            if n in temp:
                return temp.get(n)
            
            else:
                value = tri(n-1) + tri(n-2) + tri(n-3)
                temp[n] = value
                return value
            
        return tri(n)
            
            
        