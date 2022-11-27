# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
                
            stack.append(curr.val)
            curr = curr.next

        curr = res = ListNode(-1)
        
        for x in stack:
            curr.next = ListNode(x)
            curr = curr.next
        
        return res.next