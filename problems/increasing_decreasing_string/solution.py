class Solution:
    def sortString(self, S: str) -> str:
        mp = collections.defaultdict(int)
        n = len(S)
        for s in S:
            mp[s] += 1
        
        mp = dict(sorted(mp.items()))
        res = []
        while len(res) != n:
            for key in mp:
                if mp[key]:
                    res.append(key)
                    mp[key] -= 1

            for key in dict(sorted(mp.items(), reverse = True)):
                if mp[key]:
                    res.append(key)
                    mp[key] -= 1

        
        return "".join(res)
            