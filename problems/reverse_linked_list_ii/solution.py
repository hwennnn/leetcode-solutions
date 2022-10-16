# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right: return head
        
        dummy = ListNode(-1, head)
        
        prev, curr = dummy, head
        
        for _ in range(left - 1):
            prev = prev.next
            curr = curr.next
        
        res = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = res
            res = curr
            curr = temp
        
        prev.next.next = curr
        prev.next = res
        
        return dummy.next
