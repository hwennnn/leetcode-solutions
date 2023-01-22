class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(score), len(score[0])
        A = []
        
        for i, row in enumerate(score):
            A.append((-row[k], i))
        
        return [score[i] for _, i in sorted(A)]