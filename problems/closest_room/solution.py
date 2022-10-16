from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms, queries):
        Q = sorted([(y, x, i) for i, (x,y) in enumerate(queries)])[::-1]
        R = sorted((y, x) for x, y in rooms)[::-1]
        n, q = len(R), len(Q)
        p1, p2, aval, ans = 0, 0, SortedList(), [-1]*q

        while p1 <= n and p2 < q:
            if p1 < n and R[p1][0] >= Q[p2][0]:
                aval.add(R[p1][1])
                p1 += 1
            else:
                if len(aval) != 0:
                    preferred, ind = Q[p2][1], Q[p2][2]
                    i = aval.bisect(preferred)
                    
                    cands = []
                    if i > 0: cands.append(aval[i-1])
                    if i < len(aval): cands.append(aval[i])
                    ans[ind] = min(cands, key = lambda x: abs(x - preferred))

                p2 += 1

        return ans