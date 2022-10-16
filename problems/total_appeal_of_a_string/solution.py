class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        
        def go(k):
            count = total = 0
            
            for x in s:
                if x == k:
                    total += (count * (count + 1)) // 2
                    count = 0
                else:
                    count += 1
            
            total += (count * (count + 1)) // 2
            
            return (n * (n + 1)) // 2 - total
        
        res = 0
        for k in string.ascii_lowercase:
            res += go(k)
            
        return res