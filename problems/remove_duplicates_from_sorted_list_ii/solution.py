# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = curr = ListNode(-1000, head)
        
        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                p = curr.next
                val = curr.next.val
                while p and p.val == val:
                    p = p.next
                curr.next = p
                
            else:
                curr = curr.next
        
        return res.next