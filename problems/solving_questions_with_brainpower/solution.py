class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        @cache
        def go(index):
            if index >= n: return 0
            
            points, skip = questions[index]
            
            res = go(index + 1)
            res = max(res, points + go(index + skip + 1))
            
            return res
        
        return go(0)