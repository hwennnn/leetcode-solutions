class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        
        for node, out in enumerate(edges):
            scores[out] += node
        
        res = maxScore = -1
        
        for node, score in enumerate(scores):
            if score > maxScore:
                maxScore = score
                res = node
        
        return res
        