# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        ans = None
        
        
        while head:
            temp = head
            head = head.next
            temp.next = ans
            ans = temp
        
        return ans