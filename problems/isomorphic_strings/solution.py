class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def decode(s):
            dic = {}
            lst = []
            for char in s:
                if char not in dic:
                    dic[char] = len(dic)
                lst.append(dic[char])
            return str(lst)
        
        
            
        return decode(s) == decode(t)