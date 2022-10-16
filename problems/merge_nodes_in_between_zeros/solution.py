# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = res = ListNode(-1)
        
        s = 0
        head = head.next
        
        while head:
            if head.val == 0:
                curr.next = ListNode(s)
                curr = curr.next
                s = 0
            else:
                s += head.val
            
            head = head.next
        
        return res.next
        