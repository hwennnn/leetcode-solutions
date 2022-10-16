class Solution:
    def scoreOfStudents(self, s: str, A: List[int]) -> int:
            c = collections.Counter(A)
            n = len(s) // 2 + 1
            res = [[set() for _ in range(n)] for j in range(n)]
            
            for i in range(n):
                res[i][i].add(int(s[2 * i]))
                
            for dif in range(1, n):
                for start in range(n - dif):
                    end = start + dif
                    curset = set()
                    for i in range(start * 2 + 1, end * 2, 2):
                        if s[i] == "+":
                            for a in res[start][i // 2]:
                                for b in res[i // 2 + 1][end]:
                                    if a + b <= 1000:
                                        curset.add(a + b)
                        else:
                            for a in res[start][i // 2]:
                                for b in res[i // 2 + 1][end]:
                                    if a * b <= 1000:
                                        curset.add(a * b)
                    res[start][end] = curset
                    
            ans = 0
            crt = eval(s)
            for i in res[0][-1]:
                if i in c:
                    if i == crt:
                        ans += 5 * c[i]
                    else:
                        ans += 2 * c[i]
                        
            return ans