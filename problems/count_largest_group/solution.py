class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = collections.defaultdict(int)
        for i in range(1, n + 1):
            t = sum(map(int, list(str(i))))
            d[t] += 1
        return sum(1 for i in d.values() if i >= max(d.values()))
