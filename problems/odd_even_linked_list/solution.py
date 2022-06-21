# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o = odd = ListNode(-1)
        e = even = ListNode(-1)
        
        isOdd = True
        while head:
            node = ListNode(head.val)
            if isOdd:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
            
            isOdd = not isOdd
            head = head.next
        
        odd.next = e.next
        
        return o.next