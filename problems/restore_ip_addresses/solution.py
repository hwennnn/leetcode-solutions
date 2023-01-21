class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        res = []

        def go(index, curr):
            if len(curr) > 4: return
            
            if index == N and len(curr) == 4:
                res.append(".".join(curr))
                return
            
            for k in range(1, 4):
                if index + k > N: break
                word = s[index : index + k]

                if (len(word) > 1 and word[0] == "0") or int(word) > 255:
                    continue
                
                go(index + k, curr + [word])
        
        go(0, [])
        return res