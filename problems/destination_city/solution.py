class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a = set()
        
        for path in paths:
            a.add(path[1])
        
        for path in paths:
            if path[0] in a:
                a.remove(path[0])
            
        return a.pop()
            
                