class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = s = 0
        mp = collections.defaultdict(int)
        
        for i,x in enumerate(count):
            if x > 0:
                s += i * x
                mp[i] += x
                n += x
        
        mmin = min(mp)
        mmax = max(mp)
        mode = max(mp, key = mp.get)
        mean = s / n
        
        for i in range(255):
            count[i + 1] += count[i]
        
        left, right = (n - 1) // 2, n // 2
        l = bisect.bisect(count, left)
        r = bisect.bisect(count, right)
        median = (l + r) / 2
        
        return [mmin, mmax, mean, median, mode]