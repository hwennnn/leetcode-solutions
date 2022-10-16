class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dist = {}
        
        for i, x in enumerate(s):
            if x not in dist:
                dist[x] = i
            else:
                k = ord(x) - ord("a")
                
                if distance[k] != i - dist[x] - 1:
                    return False
            
        return True