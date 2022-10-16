class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        INF = 10 ** 20
        total = [0] * (1 << n)
        
        for mask in range(1 << n):
            m = 0
            for j in range(n):
                if mask & (1 << j) > 0:
                    m += cookies[j]
            total[mask] = m
        
        @cache
        def go(index, mask):
            if index == k:
                return 0 if mask == 0 else INF
            
            res = INF
            sub = mask
            
            while sub > 0:
                res = min(res, max(total[sub], go(index + 1, mask ^ sub)))
                sub = (sub - 1) & mask
        
            return res
        
        return go(0, (1 << n) - 1)