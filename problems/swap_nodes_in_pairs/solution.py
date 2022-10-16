# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = curr = ListNode(-1, head)
        
        while curr.next and curr.next.next:
            first, second = curr.next, curr.next.next
            following = curr.next.next.next
            
            curr.next, second.next, first.next = second, first, following
            
            curr = first
        
        return res.next