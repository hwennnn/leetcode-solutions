class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = {}
        
        for x in key:
            if x == " ": continue
                
            if x not in mp:
                mp[x] = chr(ord('a') + len(mp))

        res = ""
        
        for x in message:
            if x == " ":
                res += x
            else:
                res += mp[x]
        
        return res