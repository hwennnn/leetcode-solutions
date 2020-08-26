class Solution:
    def numSplits(self, s: str) -> int:
        left_count = collections.Counter()
        right_count = collections.Counter(s)
        res = 0
        for c in s:
            left_count[c] += 1
            right_count[c] -= 1
            if right_count[c] == 0:
                del right_count[c]
            
            if len(left_count) == len(right_count):
                res += 1
                
        return res
		