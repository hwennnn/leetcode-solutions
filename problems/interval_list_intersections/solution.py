class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:

        n1, n2 = len(first), len(second)
        i = j = 0
        res = []
        
        while i < n1 and j < n2:
            s1, e1 = first[i]
            s2, e2 = second[j]
            
            s, e = max(s1, s2), min(e1, e2)
            if s <= e:
                res.append([s, e])
            
            if e1 <= e2:
                i += 1
            else:
                j += 1
            
        return res