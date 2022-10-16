class Solution:
    def entityParser(self, text: str) -> str:
        d = {"&quot;" : '"', 
             "&apos;": "'",
             "&amp;": "&",
             "&gt;":">",
             "&lt;" : "<",
             "&frasl;" : "/"}

        special = ""
        res = ""
        for c in text:
            if c != "&":
                if special == "":
                    res += c
                else:
                    special += c
                    
                    if c == ";":
                        if special in d:
                            res += d[special]
                            special = ""
                        else:
                            res += special
                            special = ""
            else:
                res += special
                special = "&"
            
        return res