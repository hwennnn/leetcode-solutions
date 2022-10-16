# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        A = []
        
        while head:
            A.append(head.val)
            head = head.next
        
        res = 0
        n = len(A)
        for i in range(n // 2):
            res = max(res, A[i] + A[n - i - 1])
        
        return res