class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        R,C = len(matrix), len(matrix[0])
        mp = collections.defaultdict(collections.deque)
        
        for i in range(R):
            for j in range(C):
                if (i + j) % 2 == 0:
                    mp[i+j].appendleft(matrix[i][j])
                else:
                    mp[i+j].append(matrix[i][j])
        
        return [c for key in mp for c in mp[key]]
        