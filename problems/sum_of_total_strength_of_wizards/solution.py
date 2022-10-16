class Solution:
    def totalStrength(self, A: List[int]) -> int:
        n = len(A)
        
        right = [n] * n
        stack = []
        
        for i in range(n):
            while stack and A[i] < A[stack[-1]]:
                right[stack.pop()] = i
            
            stack.append(i)
        
        left = [-1] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and A[i] <= A[stack[-1]]:
                left[stack.pop()] = i
            
            stack.append(i)
        
        res = 0
        M = 10 ** 9 + 7
        acc = list(accumulate(accumulate(A, initial = 0)))
        
        for i, x in enumerate(A):
            l, r = left[i], right[i]
            leftSum = acc[i] - acc[max(0, l)]
            rightSum = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += A[i] * (rightSum * ln - leftSum * rn)
            res %= M
        
        return res