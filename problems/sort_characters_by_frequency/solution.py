class Solution:
    def frequencySort(self, s: str) -> str:
        A = Counter(s)
        res = []

        for k, v in sorted(A.items(), key = lambda x:-x[1]):
            res += [k] * v
        
        return "".join(res)