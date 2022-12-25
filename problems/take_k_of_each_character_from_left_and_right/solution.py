class Solution:
    def takeCharacters(self, s: str, target: int) -> int:
        N = len(s)
        
        prefix = [[0, 0, 0]]
        for x in s:
            a, b, c = prefix[-1]
            
            if x == "a":
                a += 1
            elif x == "b":
                b += 1
            else:
                c += 1
            
            prefix.append([a, b, c])
        
        def query(i, j):
            la, lb, lc = prefix[i]
            ra, rb, rc = prefix[j]
            
            return [ra - la, rb - lb, rc - lc]
        
        def good(k):
            for i in range(k + 1):
                la, lb, lc = query(0, i)
                ra, rb, rc = query(N - k + i, N)

                a, b, c = la + ra, lb + rb, lc + rc
                
                if a >= target and b >= target and c >= target:
                    return True
                
            return False
        
        res = -1
        left, right = 3 * target, N
        
        while left <= right:
            mid = left + (right - left) // 2

            if good(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res