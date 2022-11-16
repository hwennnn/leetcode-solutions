class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        N = len(message)
        parts = digits = 1
        
        def sz(x): return len(str(x))

        while parts * (sz(parts) + 3) + digits + N > parts * limit:
            if 3 + sz(parts) * 2 > limit: return []
            parts += 1
            digits += sz(parts)
        
        i = 0
        curr = 1
        res = []

        while i < N:
            suf = sz(curr) + sz(parts) + 3
            pref = limit - suf
            word = message[i : min(N, i + pref)] + "<" + str(curr) + "/" + str(parts) + ">"
            res.append(word)
            i += pref
            curr += 1
        
        return res

