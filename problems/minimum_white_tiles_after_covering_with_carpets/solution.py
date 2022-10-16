class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        total = 0
        prefix = [0]
        
        if numCarpets * carpetLen >= n: return 0
        
        for x in floor:
            if x == "1": total += 1
            prefix.append(prefix[-1] + int(x == "1"))
        
        if total == 0: return 0
            
        @cache
        def go(index, carpets):
            if index == n: return 0
            
            res = float('-inf')
            res = max(res, go(index + 1, carpets))
            
            bound = min(n, index + carpetLen)
            if carpets > 0 and prefix[bound] - prefix[index] > 0:
                res = max(res, go(bound, carpets - 1) + prefix[bound] - prefix[index])
            
            return res
        
        res = go(0, numCarpets)
        
        return total - res if total - res > 0 else 0