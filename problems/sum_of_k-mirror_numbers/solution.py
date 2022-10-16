class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def valid(x):
            res = []
            nums = x
            while x > 0:
                res.append(x % k)
                x //= k

            return res == res[::-1]
        
        ans = []
        for d in range(30):
            for i in range(10 ** d, 10 ** (d + 1)):
                x = str(i)
                s = int(x + x[::-1][1:])
                if valid(s):
                    ans.append(s)
                    if len(ans) == n:
                        return sum(ans)
            
            for i in range(10 ** d, 10 ** (d + 1)):
                x = str(i)
                s = int(x + x[::-1])
                if valid(s):
                    ans.append(s)
                    if len(ans) == n:
                        return sum(ans)
                