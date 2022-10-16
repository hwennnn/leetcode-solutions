class Solution:
    def maxArea(self, hn: int, wn: int, h: List[int], v: List[int]) -> int:
        h = [0] + sorted(h) + [hn]
        v = [0] + sorted(v) + [wn]            
        
        M = 10 ** 9 + 7
        h_diff = float('-inf')
        v_diff = float('-inf')
        
        for i in range(1, len(h)):
            h_diff = max(h_diff, h[i] - h[i - 1])
        
        for i in range(1, len(v)):
            v_diff = max(v_diff, v[i] - v[i - 1])
        
        return (h_diff * v_diff) % M