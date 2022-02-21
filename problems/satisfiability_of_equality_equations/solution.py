class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        def find(x):
            if u[x] != x:
                u[x] = find(u[x])
            
            return u[x]
        
        def union(x, y):
            u[find(u[x])] = find(u[y])
        
        u = {x : x for x in string.ascii_lowercase}
        
        for a, e, _, b in equations:
            if e == "=":
                union(a, b)
        
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)