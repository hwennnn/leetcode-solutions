class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        N = len(words)
        res = inf
        
        for i, x in enumerate(words):
            if x == target:
                left = abs(startIndex - i)
                right = N - left
                # print(words, i, left, right)
                res = min(res, min(left, right))
        
        return -1 if res == inf else res