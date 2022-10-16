class Solution:
    def maxNumberOfFamilies(self, n: int, rs: List[List[int]]) -> int:
        d = collections.defaultdict(map)
        
        for r,c in rs:
            if r not in d:
                d[r] = {c}
            else:
                d[r].add(c)
        
        res = 2 * n
        for r in d:
            ref = d[r]
            cnt = 0
            if 2 not in ref and 3 not in ref and 4 not in ref and 5 not in ref: cnt += 1
            
            if 6 not in ref and 7 not in ref and 8 not in ref and 9 not in ref: cnt += 1
            
            if 4 not in ref and 5 not in ref and 6 not in ref and 7 not in ref and cnt == 0: cnt += 1
                
            res += (cnt - 2)
        
        return res