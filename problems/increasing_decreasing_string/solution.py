class Solution:
    def sortString(self, s: str) -> str:
        dic = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        high = float('-inf')
        c = set(alphabet)
        for a in alphabet:
            dic[a] = s.count(a)
            high = max(high, dic[a])

        ans = []
    
        while high:
            for d in dic:
                if dic.get(d,0) > 0:
                    ans.append(d)
                    dic[d] = dic.get(d,0) - 1
                    if dic[d] == 0:
                        c.remove(d)
            for d in reversed(dic):
                if dic.get(d,0) > 0:
                    ans.append(d)
                    dic[d] = dic.get(d,0) - 1
                    if dic[d] == 0:
                        c.remove(d)

            high -= 1
                
                
        return "".join(ans)