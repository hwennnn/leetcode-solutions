class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = collections.defaultdict(int)
        
        for domain in cpdomains:
            count, url = domain.split()
            s = url.split('.')
            for i in range(len(s)):
                mp[".".join(s[i:])] += int(count)
        
        res = []
        
        for k, v in mp.items():
            res.append(f'{v} {k}')
        
        return res