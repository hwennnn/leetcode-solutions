class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        A = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                ssum = mul + A[p2]
                
                A[p1] += ssum // 10
                A[p2] = ssum % 10
                
        res = ""
        for c in A:
            if res or c != 0:
                res += str(c)
        
        return res or "0"