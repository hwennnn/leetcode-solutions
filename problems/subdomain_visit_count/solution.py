class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = collections.Counter()
        for cd in cpdomains:
            n, d = cd.split()
            c[d] += int(n)
            for i in range(len(d)):
                if d[i] == '.': c[d[i + 1:]] += int(n)

        return ["%d %s" % (c[k], k) for k in c]