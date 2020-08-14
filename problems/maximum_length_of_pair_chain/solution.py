class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x: x[1])
        
        cur = -math.inf
        ans = 0
        
        for head,tail in pairs:
            if head > cur:
                ans += 1
                cur = tail
        
        return ans
                