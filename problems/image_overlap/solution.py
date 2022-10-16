class Solution:
     def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(int)
        a = []
        b = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if(A[i][j] == 1):
                    a.append((i,j))
                if(B[i][j] == 1):
                    b.append((i,j))

        ans = 0
        for t1 in a:
            for t2 in b:
                t3 = (t2[1]-t1[1],t2[0]-t1[0])
                d[t3] += 1
                ans = max(ans, d[t3])
        return ans
        