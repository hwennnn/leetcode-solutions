from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, qc: str, qi: List[int]) -> List[int]:
        M = 10 ** 6
        n = len(s)
        k = len(qc)
        
        s = list(s)
        
        sl = SortedList()
        h = SortedList()
        
        curr = 0
        
        for x, group in groupby(s):
            length = sum(1 for c in group)
            sl.add((curr, curr + length - 1))
            h.add(length)
            curr += length
        
        def add(x, y):
            sl.add((x, y))
            h.add(y - x + 1)
        
        def remove(x, y):
            sl.remove((x, y))
            h.remove(y - x + 1)
        
        def split(i):
            index = sl.bisect_right((i, M)) - 1
        
            left, right = sl[index]
            remove(left, right)
            
            if left != i:
                add(left, i - 1)
                
            add(i, i)
            
            if right != i:
                add(i + 1, right)
        
        def merge(index):
            if index + 1 >= len(sl): return
            
            left1, right1 = sl[index]
            left2, right2 = sl[index + 1]
            
            if s[right1] != s[left2]: return
            
            remove(left1, right1)
            remove(left2, right2)
            add(left1, right2)
            
        res = []
        
        for i, c in zip(qi, qc):
            if s[i] == c:
                res.append(h[-1])
                continue
            
            split(i)
            
            index = sl.bisect_right((i, M)) - 1
            
            s[i] = c
            merge(index)
            
            if index - 1 >= 0:
                merge(index - 1)
            
            res.append(h[-1])
        
        return res
            
        