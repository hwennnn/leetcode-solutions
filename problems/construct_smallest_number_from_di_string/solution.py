class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        used = [False] * 10
        ans = "987654321"
        
        def dfs(index, s, prev):
            nonlocal ans
            
            if index == n:
                ss = "".join(s)
                if ss < ans:
                    ans = ss
                    
                return
            
            if pattern[index] == "I":
                for i in range(prev + 1, 10):
                    if used[i]: continue

                    used[i] = True
                    s.append(str(i))
                    dfs(index + 1, s, i)
                    used[i] = False
                    s.pop()
            else:
                for i in range(prev - 1, 0, -1):
                    if used[i]: continue

                    used[i] = True
                    s.append(str(i))
                    dfs(index + 1, s, i)
                    used[i] = False
                    s.pop()
        
        for i in range(1, 10):
            used[i] = True
            dfs(0, [str(i)], i)
            used[i] = False
        
        return ans
