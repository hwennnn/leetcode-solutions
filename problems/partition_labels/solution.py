class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        indices = {x: i for i, x in enumerate(s)}
        i = 0
        curr = set()
        res = []
        s += "!"
        
        for j, x in enumerate(s):
            if j == n or (j != 0 and len(curr) == 0):
                res.append(j - i)
                i = j
                
                if j == n: break
            
            curr.add(x)
            
            if indices[x] == j:
                curr.remove(x)
        
        
        return res
                