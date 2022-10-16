# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, rows: int, cols: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * cols for _ in range(rows)]

        i = j = 0
        d = [(0, 1), (1, 0), (0, - 1), (-1, 0)]
        dd = 0
        
        while head:
            val = head.val
            matrix[i][j] = val
            
            i += d[dd][0]
            j += d[dd][1]
            
            if i == rows or j == cols or i == -1 or j == -1 or matrix[i][j] != -1:
                i -= d[dd][0]
                j -= d[dd][1]
                
                dd = (dd + 1) % 4
                
                i += d[dd][0]
                j += d[dd][1]
            
            head = head.next
        
        return matrix