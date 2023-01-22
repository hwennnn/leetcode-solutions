class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        res = []

        def go(index, curr):
            if index == N:
                res.append(curr)
                return
            
            for j in range(index, N):
                x = s[index : j + 1]
                if x == x[::-1]:
                    go(j + 1, curr + [x])

        go(0, [])
        return res