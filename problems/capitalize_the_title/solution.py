class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []
        
        for s in title.split(" "):
            if len(s) <= 2:
                res.append(s.lower())
            else:
                res.append(s.title())
        
        return " ".join(res)