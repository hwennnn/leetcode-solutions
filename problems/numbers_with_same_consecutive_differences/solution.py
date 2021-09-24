class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        curr = range(1, 10)
        
        for _ in range(n - 1):
            temp = set()
            for x in curr:
                y = x % 10
                if y + k < 10:
                    temp.add(x * 10 + y + k)
                
                if y - k >= 0:
                    temp.add(x * 10 + y - k)
            
            curr = temp
            
        return list(curr)