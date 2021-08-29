class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        n1, n2 = len(first), len(second)
        
        while i < n1 and j < n2:
            s1, e1 = first[i]
            s2, e2 = second[j]
            
            if s1 <= e2 and s2 <= e1:
                res.append([max(s1, s2), min(e1, e2)])
            
            if e1 <= e2:
                i += 1
            else:
                j += 1
                
        return res
