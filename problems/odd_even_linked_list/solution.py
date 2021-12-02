# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddE = odd = ListNode(-1)
        headE = even = ListNode(-1)
        
        isOdd = True
        while head:
            node = ListNode(head.val)
            
            if isOdd:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
            
            head = head.next
            isOdd = not isOdd
            
        
        odd.next = headE.next
        
        return oddE.next