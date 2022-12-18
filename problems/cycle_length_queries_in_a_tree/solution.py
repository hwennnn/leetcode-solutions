class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        
        for a, b in queries:
            count = 1
            
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                    
                count += 1
            
            res.append(count)
            
        return res