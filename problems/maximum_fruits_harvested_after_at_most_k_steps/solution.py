class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], start: int, k: int) -> int:
        limits = max(max([x for (x, _) in fruits]), start) + k
        s = [0] * (limits + 1)
        
        for x, count in fruits:
            s[x] = count

        for i in range(1, limits + 1):
            s[i] += s[i - 1]
            
        res = float('-inf')
        
        for i in range(max(0, start - k), start + k + 1):
            if i <= start:
                leftover = k - (start - i)
                right = max(start, i + leftover)
                left = s[i - 1] if i >= 1 else 0
                res = max(res, s[right] - left)
            else:
                leftover = k - (i - start)
                idx = min(start, i - leftover)
                left = s[idx - 1] if idx >= 1 else 0
                res = max(res, s[i] - left)
        
        return res