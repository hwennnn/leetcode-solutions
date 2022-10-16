class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        recList = []
        
        def mergeRec(recList, curr, i):
            if len(recList) <= i:
                recList.append(curr)
                return
            
            r = recList[i]
            
            if curr[2] <= r[0] or curr[3] <= r[1] or curr[0] >= r[2] or curr[1] >= r[3]:
                mergeRec(recList, curr, i + 1)
                return
            
            if curr[0] < r[0]:
                mergeRec(recList, [curr[0], curr[1], r[0], curr[3]], i + 1)
            
            if curr[2] > r[2]:
                mergeRec(recList, [r[2], curr[1], curr[2], curr[3]], i + 1)
            
            if curr[1] < r[1]:
                mergeRec(recList, [max(curr[0], r[0]), curr[1], min(curr[2], r[2]), r[1]], i + 1)
            
            if curr[3] > r[3]:
                mergeRec(recList, [max(curr[0], r[0]), r[3], min(curr[2], r[2]), curr[3]], i + 1)
        
        for rec in rectangles:
            mergeRec(recList, rec, 0)

        res = 0

        for (x1, y1, x2, y2) in recList:
            res += (x2 - x1) * (y2 - y1)
        
        return res % M