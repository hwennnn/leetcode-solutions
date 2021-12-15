# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(float('-inf'))
        
        while head:
            curr = res
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            curr.next = ListNode(head.val, curr.next)
            head = head.next
        
        return res.next