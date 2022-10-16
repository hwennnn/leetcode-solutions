class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = len)
        s = set()
        res = []
        
        for f in folder:
            path = f.split("/")[1:]
            full = ""
            for p in path:
                full += p
                if full in s: break
            else:
                s.add(full)
                res.append(f)
    
                
        
        return res