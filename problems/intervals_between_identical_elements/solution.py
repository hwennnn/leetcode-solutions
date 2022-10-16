class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        res = []
        mp = collections.defaultdict(list)
        prefix = collections.defaultdict(list)
        
        for i, x in enumerate(arr):
            mp[x].append(i)
            prefix[x].append(i)
        
        for k, p in prefix.items():
            for i in range(1, len(p)):
                p[i] += p[i - 1]
            prefix[k] = [0] + prefix[k]
        
        for i, x in enumerate(arr):
            n = len(mp[x])
              
            index = bisect.bisect_left(mp[x], i)

            left = index * i - (prefix[x][index] - prefix[x][0])
            right = (prefix[x][-1] - prefix[x][index + 1]) - i * (n - index - 1)

            res.append(left + right)
        
        return res
        