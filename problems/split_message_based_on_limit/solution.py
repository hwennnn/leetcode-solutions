class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        N = len(message)

        def good(k):
            i = 0
            total = len(str(k))
            curr = 1
            parts = 0
            
            while i < N:
                suf = len(str(curr)) + total + 3
                pref = limit - suf
                if pref < 0: return False
                parts += 1
                i += pref
                curr += 1
            
            return parts <= k
                
        
        left, right = 1, N
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        i = 0
        curr = 1
        res = []

        while i < N:
            suf = len(str(curr)) + len(str(left)) + 3
            pref = limit - suf
            if pref < 0: return []
            word = message[i : min(N, i + pref)] + "<" + str(curr) + "/" + str(left) + ">"
            if len(word) > limit: return []
            res.append(word)
            i += pref
            curr += 1

        return res